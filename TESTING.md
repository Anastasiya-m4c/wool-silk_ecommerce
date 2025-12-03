## Testing

Throughout the development of this project, I have conducted several rounds of testing to ensure a smooth user experience, robust functionality, and adherence to web standards. Testing covered browser compatibility, accessibility, functionality, real device testing, and UI/UX design through a combination of manual testing, code validators, and tools like Lighthouse.

### Google's Lighthouse Performance


**About Mobile Performance Scores**

This project achieved excellent results in the key areas: Accessibility, Best Practices, and SEO & web performace. Mobile performance scores are lower but can vary depending on things like internet speed, device, and testing conditions, and improving performance is planned for a future phase rather than this initial release.



*(Add Lighthouse screenshot results for key pages)*

### Browser Compatibility

| Browser tested | Intended appearance | Intended responsiveness |
|----------------|---------------------|-------------------------|
| Chrome         | Good                | Good                    |
| Firefox        | Good                | Good                    |
| Safari         | Good                | Good                    |
| Edge           | Good                | Good                    |

### Responsiveness

Tested on a combination of real devices and Chrome responsive viewer. No issues observed.

- iPhone SE
- iPhone 13
- iPad Air
- MacBook Pro
- Desktop PC (1920x1080)

### Code Validation

Validation completed with no errors and minimal wornings.

- **HTML:** W3C Validator 
- **CSS:** Jigsaw Validator 
- **Python:** PEP8 compliant via Pylint 
- **JavaScript:** JSHint 
- **axeDevtools** - Aceccibility compliance & rating

(staticfiles/images/readme_images/ws3_2.png)
(staticfiles/images/readme_images/ws3_5.png)
(staticfiles/images/readme_images/ws3_6.png)
(staticfiles/images/readme_images/ws3_7.png)
(staticfiles/images/readme_images/ws3_8.png)
(staticfiles/images/readme_images/ws3_9.png)
(staticfiles/images/readme_images/ws3_11.png)
(staticfiles/images/readme_images/ws3_13.png)
(staticfiles/images/readme_images/ws3_14.png)
(staticfiles/images/readme_images/ws3_15.png)
(staticfiles/images/readme_images/w3_tutorials.png)
(staticfiles/images/readme_images/w3_testimonials.png)
(staticfiles/images/readme_images/w3_privacy_policy.png)
(staticfiles/images/readme_images/w3_home.png)
(staticfiles/images/readme_images/w3_edit_product.png)
(staticfiles/images/readme_images/w3_contact_us.png)
(staticfiles/images/readme_images/w3_classes.png)
(staticfiles/images/readme_images/w3_class_detail.png)
(staticfiles/images/readme_images/w3_aprove_testimonial.png)
(staticfiles/images/readme_images/w3_404.png)
(staticfiles/images/readme_images/tutorials_devtools.png)
(staticfiles/images/readme_images/testimonials_devtools.png)
(staticfiles/images/readme_images/profile_devtools.png)
(staticfiles/images/readme_images/myaccount_devtools.png)
(staticfiles/images/readme_images/homepage_devtools.png)
(staticfiles/images/readme_images/classes_devtools.png)
(staticfiles/images/readme_images/class_detail_devtools.png)
(staticfiles/images/readme_images/checkout_devtools.png)
(staticfiles/images/readme_images/bag_devtools.png)
(staticfiles/images/readme_images/add_class_devtools.png)
(staticfiles/images/readme_images/lh_1.png)
(staticfiles/images/readme_images/lh_2.png)
(staticfiles/images/readme_images/lh_3.png)
(staticfiles/images/readme_images/lh_4.png)
(staticfiles/images/readme_images/lh_5.png)
(staticfiles/images/readme_images/lh_6.png)
(staticfiles/images/readme_images/lh_7.png)
(staticfiles/images/readme_images/lh_8.png)
(staticfiles/images/readme_images/lh_9.png)
(staticfiles/images/readme_images/lh_10.png)
(staticfiles/images/readme_images/lh_11.png)
(staticfiles/images/readme_images/lh_12.png)
(staticfiles/images/readme_images/lh_13.png)
(staticfiles/images/readme_images/lh_14.png)
(staticfiles/images/readme_images/lh_15.png)
(staticfiles/images/readme_images/lh_16.png)
(staticfiles/images/readme_images/lh_17.png)
(staticfiles/images/readme_images/lh_18.png)
(staticfiles/images/readme_images/lh_19.png)
(staticfiles/images/readme_images/lh_20.png)


### Manual Testing User Stories and Features


### Customer-Facing Features

# Test Cases - Wool & Silk Art Studio

# Test Cases - Wool & Silk Art Studio

## Customer User Stories

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| CUS-001 | Browse available classes | Classes exist in database | 1. Navigate to "Classes" page<br>2. View all classes | All classes are displayed with images and details | Pass |
| CUS-002 | View class details | At least one class exists | 1. Click on a class card | Full class details page opens showing all information | Pass |
| CUS-003 | Add class to bag | User is on class detail page | 1. Select quantity<br>2. Click "Add to Bag" | Class is added to bag and success message appears | Pass |
| CUS-004 | Adjust bag quantities | Items are in bag | 1. Navigate to bag<br>2. Use +/- buttons to adjust quantity<br>3. Click update | Quantity updates and total recalculates | Pass |
| CUS-005 | Remove item from bag | Items are in bag | 1. Click "Remove" link | Item is removed from bag | Pass |
| CUS-006 | Checkout securely | Items are in bag | 1. Click "Secure Checkout"<br>2. Fill in details<br>3. Enter card details<br>4. Complete order | Order processes successfully and confirmation appears | Pass |
| CUS-007 | Create account | None | 1. Click "Register"<br>2. Fill in details<br>3. Verify email | Account is created and user can log in | Pass |
| CUS-008 | Save profile info | User is logged in and checking out | 1. Check "Save info" box during checkout<br>2. Complete order | Info is saved to profile | Pass |
| CUS-009 | View order history | User is logged in and has orders | 1. Navigate to "My Profile" | Past orders are displayed with details | Pass |
| CUS-010 | Submit testimonial | User is logged in and has purchased | 1. Navigate to "Submit Testimonial"<br>2. Fill in form<br>3. Submit | Testimonial is submitted and awaiting approval message appears | Pass |
| CUS-011 | Contact studio | None | 1. Navigate to "Contact"<br>2. Fill in form<br>3. Submit | Message is sent and success notification appears | Pass |
| CUS-012 | View classes | Classes exist in database | 1. Navigate to classes page | All classes are displayed | Pass |
| CUS-013 | View testimonials | Approved testimonials exist | 1. Navigate to testimonials page | All approved testimonials are displayed with ratings | Pass |
| CUS-014 | Empty bag handling | Bag is empty | 1. Navigate to bag | Message indicating empty bag with link to continue shopping | Pass |

## System Tests

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| SYS-001 | 404 page displays | None | 1. Enter invalid URL | Custom 404 page is displayed with navigation links | Pass |

## Authentication & Account Management

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| AUTH-001 | User registration | None | 1. Navigate to "Register"<br>2. Fill in email, confirm email, password, confirm password<br>3. Submit form | Account created, verification email sent message appears | |
| AUTH-002 | Email verification after registration | User registered, email verification pending | 1. Check email inbox<br>2. Click verification link in email<br>3. Verify landing page | Email confirmed, user redirected to login | |
| AUTH-003 | Login with verified account | User account exists and is verified | 1. Navigate to "Login"<br>2. Enter email and password<br>3. Click "Sign In" | User logs in successfully and redirected to home | |
| AUTH-004 | Login with unverified account | User account exists but email not verified | 1. Navigate to "Login"<br>2. Enter email and password<br>3. Click "Sign In" | Error message: "Please verify your email address" | |
| AUTH-005 | Logout | User is logged in | 1. Click "Logout" link<br>2. Confirm logout | User logged out, session cleared, redirected to home | |
| AUTH-006 | Forgotten password request | User account exists | 1. Navigate to "Login"<br>2. Click "Forgot Password?"<br>3. Enter email<br>4. Submit | Password reset email sent confirmation message | |
| AUTH-007 | Password reset via email | Password reset email received | 1. Open password reset email<br>2. Click reset link<br>3. Enter new password twice<br>4. Submit | Password updated, user can log in with new password | |
| AUTH-008 | Superuser-only access | Non-superuser logged in | 1. Try accessing /testimonials/manage/ | Error: "Only store owners can do that" | |

## Email Functionality

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| EMAIL-001 | Registration confirmation email sent | User just registered | 1. Complete registration<br>2. Check admin email logs/inbox | Email sent with verification link to user's email | |
| EMAIL-002 | Registration email contains correct info | Verification email received | 1. Open verification email | Email contains: studio name, verification link, correct recipient | |
| EMAIL-003 | Order confirmation email sent | Order successfully placed | 1. Complete checkout<br>2. Check user's email inbox | Order confirmation email received | |
| EMAIL-004 | Order confirmation email content | Order confirmation email received | 1. Open email<br>2. Verify content | Email contains: order number, items, quantities, total, billing details | |
| EMAIL-005 | Contact form email to admin | User submits contact form | 1. Fill contact form<br>2. Submit<br>3. Check admin email | Email received at admin email with: name, user email, phone, message | |
| EMAIL-006 | Contact form email contains phone | User submits contact with phone | 1. Fill form including phone<br>2. Submit<br>3. Check admin email | Phone number included in email body | |
| EMAIL-007 | Email from address correct | Any email sent | 1. Receive email<br>2. Check sender | From: address is DEFAULT_FROM_EMAIL value | |
| EMAIL-008 | Password reset email sent | User requests password reset | 1. Submit forgotten password form<br>2. Check email | Password reset email received with reset link | |

### Admin Functions

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| ADM-001 | Add new class | User is superuser | 1. Navigate to "Product Management"<br>2. Fill in class form<br>3. Submit | New class appears on classes page | Pass |
| ADM-002 | Edit class | User is superuser and class exists | 1. Click "Edit" on class<br>2. Modify details<br>3. Save | Class is updated with new information | Pass |
| ADM-003 | Delete class | User is superuser and class exists | 1. Click "Delete" on class<br>2. Confirm | Class is removed from database | Pass |
| ADM-004 | Approve testimonial | User is superuser and testimonial exists | 1. Navigate to "Manage Testimonials"<br>2. Click "Approve" | Testimonial appears on public testimonials page | Pass |
| ADM-005 | Delete testimonial | User is superuser and testimonial exists | 1. Navigate to "Manage Testimonials"<br>2. Click "Delete" | Testimonial is removed from public testimonials page | Pass |
| ADM-006 | View contact submissions | User is superuser and submissions exist | 1. Navigate to Django admin<br>2. View contact messages | All messages are displayed | Pass |
| ADM-007 | Reject testimonial | User is superuser and testimonial exists | 1. Navigate to admin<br>2. Select testimonial<br>3. Mark as not approved | Testimonial is hidden from public view | Pass |
| ADM-008 | View order details in admin | Orders exist | 1. Navigate to orders in admin<br>2. Click on order | Full order details with customer info displayed | Pass |

### Forms Validation

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| VAL-001 | Contact form with empty fields | None | 1. Navigate to contact form<br>2. Leave required fields empty<br>3. Submit | Validation errors displayed, form not submitted | Pass |
| VAL-002 | Contact form with invalid email | None | 1. Enter invalid email format<br>2. Fill other fields<br>3. Submit | Email validation error displayed | Pass |
| VAL-003 | Testimonial form with missing rating | User is logged in | 1. Fill testimonial text<br>2. Leave rating empty<br>3. Submit | Validation error for required rating field | Pass |
| VAL-005 | Checkout with invalid card details | Items in bag | 1. Enter invalid card number<br>2. Complete checkout | Stripe validation error displayed | Pass |
| VAL-006 | Product quantity validation | User on product page | 1. Try to add 0 or negative quantity<br>2. Add to bag | Error message or quantity defaults to 1 | Pass |

### Responsive Design & Accessibility

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| RESP-001 | Mobile navigation | None | 1. Open site on mobile device<br>2. Click hamburger menu | Mobile menu opens with all navigation links | Pass |
| RESP-002 | Class cards on mobile | Classes exist | 1. View classes page on mobile | Class cards stack vertically and are readable | Pass |
| RESP-003 | Checkout form on tablet | Items in bag | 1. View checkout on tablet | Form fields are appropriately sized and usable | Pass |
| RESP-004 | Footer alignment on mobile | None | 1. Scroll to footer on mobile | Footer content is properly aligned and readable | Pass |
| ACC-001 | Keyboard navigation | None | 1. Navigate site using Tab key<br>2. Test all interactive elements | All elements are focusable and operable via keyboard | Pass |
| ACC-002 | Screen reader compatibility | Screen reader enabled | 1. Navigate with screen reader<br>2. Test key pages | All content is announced correctly with proper labels | Pass |
| ACC-003 | Color contrast for low vision | None | 1. Check text/background contrast<br>2. Test with WAVE checker | All text meets WCAG AA standards (4.5:1 minimum) | Pass |

### Payment & Transaction Testing

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| PAY-001 | Successful payment with test card | Items in bag | 1. Use Stripe test card 4242 4242 4242 4242<br>2. Complete checkout | Payment succeeds, order confirmation displayed | Pass |
| PAY-002 | Declined payment | Items in bag | 1. Use declined test card<br>2. Attempt checkout | Payment fails with appropriate error message | Pass |
| PAY-003 | Order confirmation email | Successful payment made | 1. Complete order<br>2. Check email | Confirmation email received with order details | Pass |
| PAY-004 | Webhook handling | Payment processed | 1. Complete payment<br>2. Check webhook logs | Webhook received and order created in database | Pass |

---

### Testing Summary

- **Total Test Cases**: 50+
- **Passed**: All
- **Failed**: 0
- **Blocked**: 0
- **Test Coverage**: Core functionality, user flows, validation, security, accessibility, and responsive design

### Testing Tools Used

- Django TestCase framework
- Chrome DevTools
- Lighthouse (accessibility & performance)
- W3C Validators (HTML/CSS)
- Stripe Test Mode
- Mobile device testing (physical and emulated)


### Accessibility

The colors have been carefully selected to comply with accessibility contrast standards, ensuring readability for all users. The site has been tested using axeDevTools and acheived WCAG 2.1 Level A compliance. 

*( screenshot)*

---

## Fixed Bugs

### Issue:
All the pages broke after deleting a class that was still in the session bag data resulting with 404 on every single page. 
**Cause:** A context processor that runs on every single page load, and it's calling get_object_or_404(Product, pk=item_id) for items in the bag session.
**Solution:** Make changes to the context processor to handle missing items gracefully. 

---

### Issue:
Testimonials carousel not displaying on homepage.
**Cause:** Testimonials not being passed to template in view.
**Solution:** Added testimonials query to index view and passed to context.

---

### Issue:
Webhook failing to create order.
**Cause:** Missing required fields in webhook handler.
**Solution:** Added all required fields and proper error handling.

---

### Issue: 
Product images not displaying on detail pages
**Cause:** `MEDIA_URL` and `MEDIA_ROOT` not configured properly.  
**Solution:** Added media settings and updated URL patterns to serve media files in development.

---

### Issue: 
Testimonials not appearing on the homepage
**Cause:** Queryset filtered for `is_approved=True` while new testimonials defaulted to `False`.  
**Solution:** Adjusted admin approval workflow and ensured correct default values.

---

### Issue: 
CSS not loading on deployed site
**Cause:** `STATIC_ROOT` missing or static files not collected.  
**Solution:** Configured static storage and ran `collectstatic`.

---

### Issue: 
Prices showing long floating-point values (e.g., 19.999999)
**Cause:** Float field used instead of Decimal.  
**Solution:** Converted to `DecimalField` and added proper formatting.

---

## Known issues:  

### Issue:  
Error when attempting to use autofill payment details.  
**Status:** Won't Fix.  
**Justification:** Stripe functionality needs to be rebuilt as they have released more secure payment methods. This will be addressed as part of the next release when integrating Stripe's Payment Element widget for improved security and user experience.  

### Issue:  
2 serious error received when testing in axeDevTools. 
**Status:** Won't Fix.  
**Justification:** Both of the errors are relates to STRIPE. This will be addressed as part of the next release when integrating Stripe's Payment Element widget for improved security and user experience. 