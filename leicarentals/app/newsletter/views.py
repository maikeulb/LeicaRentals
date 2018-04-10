from flask import (
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import login_required
from app.newsletter.forms import NewsletterForm
from app.newsletter import newsletter
from app.models import (
    Customer
)
from app.tasks import send_newsletter


@newsletter.route('/', methods=['GET', 'POST'])
@newsletter.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = NewsletterForm()
    if form.validate_on_submit():
        customers = \
            Customer.query.filter_by(is_signed_up=True).all()
        emails = [c.email for c in customers]
        names = [c.first_name.title() for c in customers]
        subject = form.subject.data
        message = form.message.data
        for i in range(0, len(emails)):
            body = render_template(
                'email/newsletter.html', name=names[i], message=message)
            send_newsletter(subject,
                            [emails[i]],
                            body)
        flash('Sending newsletters')
        return redirect(url_for('customers.index'))

    return render_template('newsletter/index.html',
                           form=form,
                           title='Customers')
