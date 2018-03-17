import sys
import os
import click
from app.extensions import db
from config import Config
from app.models import (
    User,
    Mount,
    FocalLength,
    Lens,
    MembershipType,
    Customer,
)
from flask import current_app
from datetime import date
from random import choice, shuffle, sample


def register(app):
    @app.cli.command('seed-db')
    @click.command()
    def seed():
        print('Starting DB seed')
        db.drop_all()
        db.create_all()

        seed_users()

        seed_membership_types()
        seed_customers()

        seed_mounts()
        seed_focal_lengths()
        seed_lenses()

        db.session.commit()
        print('DB seed complete')

    def seed_users():
        print('Adding demo-user')
        demo = User(
            username='demo',
            password=Config.DEMO_PASSWORD,
            email=Config.DEMO_EMAIL)
        db.session.add(demo)

    def seed_mounts():
        print('Adding Mounts')

        names = ['M', 'LTM']

        for m in range(0, len(names)):
            db.session.add(Mount(name=names[m]))

    def seed_focal_lengths():
        print('Adding Focal Lengths')

        names = ['21mm', '35mm', '50mm']

        for m in range(0, len(names)):
            db.session.add(FocalLength(name=names[m]))

    def seed_membership_types():
        print('Adding Membership Types')

        names = ['Bronze', 'Gold', 'Platinum']
        sign_up_fees = [50, 80, 90]
        duration_in_months = [12, 12, 12]
        discount_rates = [0, 0, 0]

        for m in range(0, len(names)):
            db.session.add(MembershipType(name=names[m],
                                          sign_up_fee=sign_up_fees[m],
                                          duration_in_months=duration_in_months[m],
                                          discount_rate=discount_rates[m]))

    def seed_customers():
        print('Adding Customers')

        first_names = ['nik', 'kim', 'amy', 'marco', 'jake', 'allison', 'eva',
                       'com', 'elizier', 'nylah', 'marissa', 'camerson',
                       'andrea', 'keon']

        last_names = ['klaw', 'lowe', 'kombrough', 'ramsburg', 'mathews',
                      'braun', 'hunger', 'folwers', 'gross', 'barber',
                      'stanton', 'mckinney', 'craig', 'stone']

        emails = ['klaw@example.com',
                  'lowe@example.com',
                  'kombrough@example.com',
                  'ramsburg@example.com',
                  'mathews@example.com',
                  'braun@example.com',
                  'hunger@example.com',
                  'folwers@example.com',
                  'gross@example.com',
                  'barber@example.com',
                  'stanton@example.com',
                  'mckinney@example.com',
                  'craig@example.com',
                  'stone@example.com']

        membership_type_ids = [1, 2, 3]

        is_signed_up_choices = [True, False]

        date_of_births = [date(1987, 1, 2),
                          date(1987, 5, 2),
                          date(1987, 2, 3),
                          date(1991, 3, 8),
                          date(1991, 1, 9),
                          date(1991, 3, 10),
                          date(1996, 12, 12),
                          date(1996, 1, 2),
                          date(1996, 2, 3),
                          date(1996, 1, 1),
                          date(1985, 8, 8),
                          date(1985, 10, 2),
                          date(1985, 10, 1),
                          date(1985, 10, 1)]

        for c in range(0, len(last_names)):
            db.session.add(Customer(first_name=first_names[c],
                                    last_name=last_names[c],
                                    email=emails[c],
                                    membership_type_id=choice(
                                        membership_type_ids),
                                    is_signed_up=choice(is_signed_up_choices),
                                    date_of_birth=date_of_births[c]))

    def seed_lenses():
        print('Adding Lenses')

        names = ['Super Angulon',
                 'Summicron', 'Summilux',
                 'Elmar', 'Summicron', 'Summilux', 'Noctilux',
                 'Super Angulon',
                 'Summaron',
                 'Elmar', 'Summar', 'Summitar', 'Summicron']

        dates_added = [date(2011, 1, 2),
                       date(2016, 5, 2),
                       date(2016, 5, 2),
                       date(2016, 5, 2),
                       date(2016, 5, 2),
                       date(2016, 5, 2),
                       date(2015, 5, 2),
                       date(2011, 2, 3),
                       date(2011, 2, 3),
                       date(2011, 2, 3),
                       date(2011, 2, 3),
                       date(2011, 2, 3),
                       date(2015, 10, 1)]

        release_dates = [date(1950, 1, 2),
                         date(1950, 5, 2),
                         date(1950, 5, 2),
                         date(1950, 5, 2),
                         date(1950, 5, 2),
                         date(1950, 5, 2),
                         date(1950, 5, 2),
                         date(1930, 2, 3),
                         date(1930, 2, 3),
                         date(1930, 2, 3),
                         date(1930, 2, 3),
                         date(1930, 2, 3),
                         date(1930, 10, 1)]

        numbers_in_stock = [10, 13, 11, 11, 11, 12, 11, 13, 12, 11, 13, 11, 12]
        numbers_available = [10, 13, 11, 11,
                             11, 12, 11, 13, 12, 11, 13, 11, 12]
        mount_ids = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
        focal_length_ids = [1, 2, 2, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3]

        for c in range(0, len(names)):
            db.session.add(Lens(name=names[c],
                                date_added=dates_added[c],
                                release_date=release_dates[c],
                                number_in_stock=numbers_in_stock[c],
                                number_available=numbers_available[c],
                                mount_id=mount_ids[c],
                                focal_length_id=focal_length_ids[c]))
