from behave import when, then, given

from customer_service.model.customer import Customer

@when('I update customer with ID "{customer_id:d}" surname to "{surname}"')
def update_customer(context, customer_id, surname):
    response = context.web_client.post(
        '/customers/update',
        json={'customer_id': customer_id, 'surname': surname})
    assert response.status_code == 201, response.status_code
    context.response = context.web_client.get(f'/customers/{customer_id}')

