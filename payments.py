# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

charge = stripe.Charge.create(
  amount=999,
  currency='usd',
  source='tok_visa',
  receipt_email='jenny.rosen@example.com',
)