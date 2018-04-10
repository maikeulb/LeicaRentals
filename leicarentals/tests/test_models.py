class TestUserModel:

    def test_set_password(self, user):
        user.set_password('password')
        assert user.check_password('password') is True


class TestRentalModel:

    def test_can_to_dict(self, rental):
        data = rental.to_dict()
        assert data['lens_name'] == rental.lens.lens_name

    def test_can_from_to_dict(self, rental):
        data = {}
        data['lens_id'] = 1
        data['customer_id'] = 2
        rental.from_dict(data)
        assert rental.customer_id == data['customer_id']
        assert rental.lens_id == data['lens_id']


class TestLensModel:

    def test_can_to_dict(self, lens):
        data = lens.to_dict()
        assert data['id'] == lens.id

    def test_can_from_to_dict(self, lens):
        data = {}
        data['name'] = "summicron"
        lens.from_dict(data)
        assert lens.name == data['name']


class TestCustomerModel:

    def test_can_to_dict(self, customer):
        data = customer.to_dict()
        assert data['first_name'] == customer.first_name

    def test_can_from_to_dict(self, customer):
        data = {}
        data['first_name'] = 'first_name_example'
        data['last_name'] = 'last_name_example'
        customer.from_dict(data)
        assert customer.first_name == data['first_name']
        assert customer.last_name == data['last_name']
