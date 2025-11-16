# Wool & Silk Art Studio

![Wool & Silk Brand Identity](#)

View live website [HERE](#)

## About

**Wool & Silk Art Studio** Wool & Silk Art Studio is an e-commerce platform I built for my mum, Svetlana Lilley, and her wet felting art studio in Briton Ferry, Neath, South Wales. The site allows her students to browse, book, and pay for felting classes while discovering the beautiful art of working with wool and silk.  

The inspiration for Wool & Silk came from watching my mum pour her heart into her craft and wanting to give her a professional online home that truly represents her work. As a master felting artist specializing in nuno felting and working with locally sourced Welsh wool, she needed more than just a website—she needed a platform that captured the warmth and creativity of her studio while making it easy for students to join her classes. This project became my way of supporting her passion and helping her small business thrive.  

Built with **Django** and designed to be fully responsive and mobile-friendly, Wool & Silk offers a seamless experience for both my mum and her students, no matter what device they're using.  

---

## Table Of Contents:

1. [Design & Planning](#design--planning)
   - [User Stories](#user-stories)
   - [Wireframes](#wireframes)
   - [Typography](#typography)
   - [Colour Scheme](#colour-scheme)
2. [Features](#features)
   - [User Features](#user-features)
   - [Security Features](#security-features)
3. [Data Schema](#data-schema)
4. [Technologies](#technologies)
   - [Languages Used](#languages-used)
   - [Frameworks, Libraries and Programmes Used](#frameworks-libraries-and-programmes-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)

---

## Overview

Wool & Silk Art Studio is a full-stack e-commerce application built with Django. The platform showcases wet felting classes taught by master felting artist Svetlana Lilley, who specializes in nuno felting and working with locally sourced Welsh wool.

### Project Goals

- Provide an intuitive booking system for felting classes

---

## User Experience (UX)

### Target Audience

- **Craft enthusiasts** looking to learn felting techniques
- **Beginners** interested in textile arts
- **Experienced artists** wanting to master nuno felting
- **Local residents** in South Wales seeking creative workshops
- **Gift buyers** looking for unique experience gifts

### User Stories

# Wool & Silk User Stories

## Accounts & Authentication
- As a visitor, I want to create an account so that I can book classes and access tutorials.
- As a registered user, I want to log in/out securely so that I can access my purchases.
- As a user, I want to manage my profile (name, email, preferences) so I can keep my account up to date.

## In-Person Classes
- As a visitor, I want to view a list of upcoming in-person classes so I can decide what to attend.
- As a user, I want to view details of a class (date, time, location and price) so I can choose the right one for me.
- As a user, I want to book and pay a deposit for a class so I can secure my spot.
- As a user, I want to see my booked classes in my profile so I don't forget.

## Video Tutorials
- As a visitor, I want to browse tutorials selection so I can decide what to purchase.
- As a user, I want to purchase a video tutorial so I can watch it anytime.
- As a user, I want my purchased/subscribed tutorials available in my account so I can rewatch them later.

## Payments & Subscription
- As a user, I want to pay securely online (Stripe) so I feel confident using the site.
- As an admin, I want to manage prices and products so I can update offers quickly.

## Testimonials
- As a visitor, I want to read testimonials from other customers so I feel reassured about the quality of classes.
- As a user, I want to submit a testimonial after taking a class/tutorial so I can share my experience.
- As an admin, I want to moderate testimonials so I can control what gets published.

## Enquiries / Contact
- As a visitor, I want to fill in a contact/enquiry form so I can ask about classes or tutorials.
- As a user, I want to receive a confirmation email after submitting an enquiry so I know it went through.
- As an admin, I want to receive enquiries in my dashboard or by email so I can respond.

## Content & Navigation
- As a visitor, I want to see an attractive homepage with Wool & Silk's brand and offerings so I understand what's available.
- As a visitor, I want to view list and individual product.

## Admin & Management
- As an admin, I want to create, edit, and delete in-person classes so I can keep the schedule updated.
- As an admin, I want to upload/manage video tutorials so I can grow the library.
- As an admin, I want to view bookings and enquiries so I can manage operations smoothly.

---

## Future Developments

- **Tutorials Section:** Video content for learning felting techniques at home. 
- **Waiting List:** Allow customers to join a waiting list for fully booked classes
- **Class Capacity Management:** Automatic booking limits to prevent overbooking
- **Multiple Images per Class:** Gallery view for each class showing examples
- **Blog:** Tips, techniques, and studio news
- **Newsletter Signup:** Email marketing integration for updates
- **Gift Vouchers:** Purchasable class vouchers for gifts
- **Workshop Calendar:** Interactive booking calendar view
- **Social Media Integration:** Direct sharing to Instagram and Facebook

---

## Wireframes

This site is designed to be clean, welcoming, and easy to navigate, reflecting the creative and approachable nature of the studio.

[WEB](#)
[Deployed on Heroku](#)

Final MVP version:

[Finall website images](#)

---

## Typography

For the Wool & Silk website, the fonts chosen are **Bodoni Moda** and **Merriweather**, both elegant serif fonts that convey artistry and craftsmanship. Bodoni Moda is used for headings, providing a sophisticated and timeless feel, while Merriweather ensures excellent readability for body text across all devices.

This typography choice balances professionalism with warmth, reflecting the artistic nature of felting while maintaining a welcoming and trustworthy experience for users.

---

## Colour Scheme & Logo

The color scheme for Wool & Silk has been carefully selected to reflect the creative, warm, and playful nature of the studio. As my mum is partially sighted, good contrast and visibility are very important considerations in the design. The palette features vibrant blues, corals, yellows, and turquoise, inspired by the colorful nature of felted wool and the cheerful sheep mascot that represents the studio.

**Color Palette:**
- **Primary Blue (#002b68):** Trust and creativity
- **Light Blue (#3EA8C2):** Calm and trust
- **Orange (#FF8120):** Energy and inspiration
- **Cinnamon (#FF5B3C):** Warmth and approachability
- **Yellow (#rgb(255, 191, 40)):** Joy and optimism

The colors ensure strong contrast while creating a cohesive, vibrant brand identity. This thoughtfully curated palette supports an intuitive user experience, keeping focus on the classes and studio offerings.

---

## Features

### User Features

- User registration and authentication with email verification via Django Allauth
- Full CRUD functionality for classes (admin only)
- Browse classes with images, descriptions, dates, and pricing
- Add classes to shopping bag with quantity selection
- Secure checkout with Stripe payment integration
- Save delivery information for faster checkout
- View order history in user profile
- Submit testimonials with star ratings (purchase required)
- Admin approval system for testimonials before public display
- Contact form with email notifications to studio owner
- Testimonials carousel on homepage
- Pagination for browsing classes
- Responsive design ensuring usability across all devices
- Toast notifications for user feedback on actions
- Custom 404 error page
- Shopping bag preview in toast messages
- Order confirmation emails

### Security Features

Security has been carefully considered throughout the design and development of this e-commerce platform to protect both users and sensitive data. Key security measures include:

- **User Authentication and Authorization:** The application uses Django's built-in authentication system, enhanced with `django-allauth` for secure user registration, login, and email verification. Certain actions such as adding, editing, or deleting classes are restricted to superuser accounts only.

- **Ownership Verification:** Users can only edit their own profile information and view their own order history. Testimonials are linked to user accounts and can only be submitted by customers who have made a purchase.

- **Secure Payment Processing:** All payment data is handled by Stripe and never stored on the server. The application uses Stripe's secure payment intent API with webhook verification.

- **Secure Secret Management:** Sensitive data such as secret keys, database URLs, Stripe keys, and AWS credentials are managed through environment variables and not hard-coded.

- **CSRF Protection:** Django's built-in CSRF protection is enabled on all forms.

- **Webhook Signature Verification:** Stripe webhooks are verified using signature authentication to ensure they originate from Stripe.

- **Admin Approval for Testimonials:** Testimonials require admin approval before being published, ensuring content quality and preventing inappropriate submissions.

---

## Data Schema

### Entities and Attributes

- **User** (Django built-in)
  - id (Primary Key)
  - username
  - email
  - password

- **Class**
  - id (Primary Key)
  - name
  - description
  - price (DecimalField)
  - image (ImageField)
  - start_date (DateField)
  - start_time (TimeField)
  - duration (IntegerField - hours)
  - location (CharField)

- **Order**
  - id (Primary Key)
  - order_number (CharField - 8 chars, UUID-based)
  - user_profile (ForeignKey to UserProfile)
  - full_name (CharField)
  - email (EmailField)
  - phone_number (CharField)
  - country (CountryField)
  - postcode (CharField)
  - town_or_city (CharField)
  - street_address1 (CharField)
  - street_address2 (CharField)
  - date (DateTimeField)
  - order_total (DecimalField)
  - original_bag (TextField - JSON)
  - stripe_pid (CharField)

- **OrderLineItem**
  - id (Primary Key)
  - order (ForeignKey to Order)
  - product (ForeignKey to Class)
  - quantity (PositiveIntegerField)
  - lineitem_total (DecimalField - calculated)

- **UserProfile**
  - id (Primary Key)
  - user (OneToOneField to User)
  - default_full_name (CharField)
  - default_email (EmailField)
  - default_phone_number (CharField)
  - default_street_address1 (CharField)
  - default_street_address2 (CharField)
  - default_postcode (CharField)
  - default_town_or_city (CharField)
  - default_country (CountryField)

- **ContactMessage**
  - id (Primary Key)
  - name (CharField)
  - email (EmailField)
  - phone (CharField)
  - subject (CharField)
  - message (TextField)
  - created_at (DateTimeField)

- **Testimonial**
  - id (Primary Key)
  - user (ForeignKey to User)
  - title (CharField)
  - content (TextField)
  - rating (IntegerField - choices 1-5)
  - is_approved (BooleanField)
  - created_at (DateTimeField)

### Relationships

- A **User** can have one **UserProfile** (One-to-One)
- A **User** can create multiple **Orders** (One-to-Many)
- A **User** can create one **Testimonial** (One-to-Many with business rule)
- An **Order** can have multiple **OrderLineItems** (One-to-Many)
- A **Class** can appear in multiple **OrderLineItems** (One-to-Many)

---

## Technologies

### Languages Used

- **HTML5** - To create site structure
- **CSS** - To create custom styles
- **JavaScript** - For interactivity and Stripe integration
- **Python** - Backend logic and Django framework
- **Markdown** - To create README file

### Frameworks, Libraries and Programmes Used

- **Django 5.2.6** - The web framework used to develop the full-stack application
- **Bootstrap 5.0.2** - CSS framework for responsive design
- **jQuery 3.5.1** - JavaScript library for DOM manipulation
- **Font Awesome** - For icons throughout the site
- **Google Fonts** - For custom typography (Bodoni Moda, Merriweather)
- **Stripe** - Payment processing integration
- **AWS S3** - Cloud storage for static and media files
- **Heroku** - Cloud platform for hosting and deployment
- **GitPod/VS Code** - To develop the project and organize version control
- **Git/GitHub** - Version control and code repository
- **Chrome DevTools** - For debugging and testing
- **Lighthouse** - For performance testing
- **Favicon.io** - To create favicon
- **ChatGPT** - For generating content, documentation assistance & troubleshooting.

### Installed Django Apps & Libraries

- `django-allauth` - User authentication and social login
- `crispy-forms` and `crispy-bootstrap5` - Improved form styling
- `django-countries` - Country field for addresses
- `django-storages` - S3 integration for file storage
- `boto3` - AWS SDK for Python
- `Pillow` - Image processing
- `Stripe` - Payment processing
- `Gunicorn` - WSGI HTTP server for production
- `Psycopg2` - PostgreSQL database adapter
- `Whitenoise` - Static file serving (development)

---


## Testing

Throughout the development of this project, I have conducted several rounds of testing to ensure a smooth user experience, robust functionality, and adherence to web standards. Testing covered browser compatibility, accessibility, functionality, real device testing, and UI/UX design through a combination of manual testing, code validators, and tools like Lighthouse.

### Google's Lighthouse Performance

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

Validation completed with minimal errors.

- **HTML:** W3C Validator 
- **CSS:** Jigsaw Validator 
- **Python:** PEP8 compliant via Pylint 
- **JavaScript:** JSHint 

### Manual Testing User Stories and Features


### Customer-Facing Features

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| CUS-001 | Browse available classes | Classes exist in database | 1. Navigate to "Classes" page<br>2. View all classes | All classes are displayed with images and details | Pass |
| CUS-002 | View class details | At least one class exists | 1. Click on a class card | Full class details page opens showing all information | Pass |
| CUS-003 | Add class to bag | User is on class detail page | 1. Select quantity<br>2. Click "Add to Bag" | Class is added to bag and success message appears | Pass |
| CUS-004 | Adjust bag quantities | Items are in bag | 1. Navigate to bag<br>2. Use +/- buttons to adjust quantity<br>3. Click update | Quantity updates and total recalculates | Pass |
| CUS-005 | Remove item from bag | Items are in bag | 1. Click "Remove" link | Item is removed from bag | Pass |
| CUS-006 | Checkout securely | Items are in bag | 1. Click "Secure Checkout"<br>2. Fill in details<br>3. Enter card details<br>4. Complete order | Order processes successfully and confirmation appears | Pass |
| CUS-007 | Create account | None | 1. Click "Register"<br>2. Fill in details<br>3. Verify email | Account is created and user can log in | Pass |
| CUS-008 | Save delivery info | User is logged in and checking out | 1. Check "Save info" box during checkout<br>2. Complete order | Info is saved to profile | Pass |
| CUS-009 | View order history | User is logged in and has orders | 1. Navigate to "My Profile" | Past orders are displayed with details | Pass |
| CUS-010 | Submit testimonial | User is logged in and has purchased | 1. Navigate to "Submit Testimonial"<br>2. Fill in form<br>3. Submit | Testimonial is submitted and awaiting approval message appears | Pass |
| CUS-011 | Contact studio | None | 1. Navigate to "Contact"<br>2. Fill in form<br>3. Submit | Message is sent and success notification appears | Pass |
| CUS-012 | Search for classes | Classes exist in database | 1. Enter search term in search bar<br>2. Submit search | Relevant classes matching search term are displayed | Pass |
| CUS-013 | Filter classes by category | Multiple categories exist | 1. Click on category filter<br>2. Select category | Only classes in selected category are shown | Pass |
| CUS-014 | Sort classes by price | Multiple classes exist | 1. Use sort dropdown<br>2. Select "Price (Low to High)" | Classes are sorted correctly by price ascending | Pass |
| CUS-015 | View testimonials | Approved testimonials exist | 1. Navigate to testimonials page | All approved testimonials are displayed with ratings | Pass |
| CUS-016 | Empty bag handling | Bag is empty | 1. Navigate to bag | Message indicating empty bag with link to continue shopping | Pass |
| SYS-001 | 404 page displays | None | 1. Enter invalid URL | Custom 404 page is displayed with navigation links | Pass |


### Admin Functions

| Test Case ID | User Story | Preconditions | Test Steps | Expected Result | Status |
|--------------|------------|---------------|------------|-----------------|--------|
| ADM-001 | Add new class | User is superuser | 1. Navigate to "Product Management"<br>2. Fill in class form<br>3. Submit | New class appears on classes page | Pass |
| ADM-002 | Edit class | User is superuser and class exists | 1. Click "Edit" on class<br>2. Modify details<br>3. Save | Class is updated with new information | Pass |
| ADM-003 | Delete class | User is superuser and class exists | 1. Click "Delete" on class<br>2. Confirm | Class is removed from database | Pass |
| ADM-004 | Approve testimonial | User is superuser and testimonial exists | 1. Navigate to "Manage Testimonials"<br>2. Click "Approve" | Testimonial appears on public testimonials page | Pass |
| ADM-005 | View contact submissions | User is superuser and submissions exist | 1. Navigate to Django admin<br>2. View contact messages | All messages are displayed | Pass |
| ADM-006 | Reject testimonial | User is superuser and testimonial exists | 1. Navigate to admin<br>2. Select testimonial<br>3. Mark as not approved | Testimonial is hidden from public view | Pass |
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

- **Total Test Cases**: 40+
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

The colors have been carefully selected to comply with accessibility contrast standards, ensuring readability for all users. The site has been tested using the WAVE plugin on Chrome.

*(WAVE screenshot)*

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

## Deployment

The site was deployed to Heroku using the following method:

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate 
   ```

2. **Install required Python packages:**
   ```bash
   pip install django gunicorn dj-database-url psycopg2-binary
   pip install django-allauth django-crispy-forms crispy-bootstrap5
   pip install stripe pillow boto3 django-storages django-countries
   pip freeze > requirements.txt
   ```

3. **Create a new Django project:**
   ```bash
   django-admin startproject wool_and_silk .
   ```

4. **Create Django apps:**
   ```bash
   python manage.py startapp home
   python manage.py startapp classes
   python manage.py startapp bag
   python manage.py startapp checkout
   python manage.py startapp profiles
   python manage.py startapp contact
   python manage.py startapp testimonials
   ```

5. **Register apps in `settings.py`:**
   Add all apps to `INSTALLED_APPS` list.

6. **Make and apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a Django superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

9. **Create a `Procfile` in the project root:**
   ```
   web: gunicorn wool_and_silk.wsgi
   ```

10. **Update `settings.py` for Heroku:**
    - Configure database with dj_database_url
    - Set ALLOWED_HOSTS
    - Configure static and media files for AWS S3

11. **Login to Heroku:**
    ```bash
    heroku login
    ```

12. **Create Heroku app:**
    ```bash
    heroku create wool-and-silk
    ```

13. **Add PostgreSQL database:**
    ```bash
    heroku addons:create heroku-postgresql:mini
    ```

14. **Set Config Vars in Heroku:**
    - Log into Heroku dashboard
    - Go to 'Settings' tab
    - Click 'Reveal Config Vars'
    - Add all required environment variables:
      - SECRET_KEY
      - DATABASE_URL
      - STRIPE_PUBLIC_KEY
      - STRIPE_SECRET_KEY
      - STRIPE_WH_SECRET
      - AWS_ACCESS_KEY_ID
      - AWS_SECRET_ACCESS_KEY
      - USE_AWS=True

15. **Connect GitHub repository:**
    - Log into Heroku dashboard
    - Go to 'Deploy' tab
    - Connect to GitHub
    - Select wool-silk-ecommerce repository

16. **Deploy to Heroku:**
    - Click 'Deploy Branch'
    - Wait for deployment to finish
    - Click 'Open app' at the top of the screen

17. **Done!** Wool & Silk is now live.

### Creating Repository on GitHub

1. First make sure you are signed into [GitHub](https://github.com/) and go to the Code Institute template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
2. Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
3. Once the repository was created, I clicked the green **Gitpod** button to create a workspace in Gitpod so that I could write the code for the site.
4. Use terminal command to link it to VS Code.

### Deploying on Heroku


---

## Attribution

- The initial setup and e-commerce functionality of this project was strongly inspired by the Code Institute Boutique Ado walkthrough project.
- Bootstrap was used as the foundation for the base templates, then extensively customized to achieve the desired design.
- Stripe integration followed Stripe's official documentation and best practices.
- AI used for generating content, documentation assistance, and troubleshooting errors.
- AI used for implementing comlex logic for locking transaction durring checkout & updating webhook handler to adheer to new logic.  

---

## Special Thanks

**Svetlana Lilley** - For trusting me with her studio's online presence and providing all the creative inspiration.

**Alice** - For creating a fun logo and colour suggestions. 

**Code Institute** - For the comprehensive curriculum and support.

**Marco** - For continuous support, limitless resources and inspiration.

**My Mentor** - For guidance and feedback throughout the project.

**My Family** - For continuous support and motivation.

---