# Bug Report: Checkout Allowed with Empty Cart

## Summary

The system allows a user to begin the checkout process even when the shopping cart is empty, which is not expected behavior for an e-commerce application.

## Steps to Reproduce

1. Log in with valid credentials:
   - Username: `standard_user`
   - Password: `secret_sauce`
2. Do **not** add any items to the cart
3. Click on the cart icon (top-right)
4. Click the "Checkout" button

## Expected Result

User should not be able to proceed to checkout when the cart is empty.  
A message like "Your cart is empty" should be shown or the checkout button should be disabled.

## Actual Result

User is navigated to the checkout information page even though no items are in the cart.

## Severity: Medium  
## Priority: Medium

## Environment

- Browser: Chrome 125.0  
- OS: macOS Ventura  
- URL: https://www.saucedemo.com

## Notes

This could lead to confusion or incorrect orders in a real-world scenario. Most e-commerce platforms prevent checkout with an empty cart.




