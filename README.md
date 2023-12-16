# django-vendor-management
A Vendor Management System built with Django and Django REST Framework. This system handles vendor profiles, purchase order tracking, and calculates vendor performance metrics.

# Django Vendor Management System

## Overview

The Django Vendor Management System is a web application built using Django and Django REST Framework. It provides a comprehensive solution for managing vendor profiles, tracking purchase orders, and evaluating vendor performance metrics.

## Features

- Vendor Profile Management
- Purchase Order Tracking
- Vendor Performance Evaluation

## Data Models

### Vendor Model

The `Vendor` model stores essential information about each vendor, including performance metrics.

- `name`: Vendor's name.
- `contact_details`: Contact information of the vendor.
- `address`: Physical address of the vendor.
- `vendor_code`: A unique identifier for the vendor.
- `on_time_delivery_rate`: Tracks the percentage of on-time deliveries.
- `quality_rating_avg`: Average rating of quality based on purchase orders.
- `average_response_time`: Average time taken to acknowledge purchase orders.
- `fulfillment_rate`: Percentage of purchase orders fulfilled successfully.

### Purchase Order Model

The `PurchaseOrder` model captures the details of each purchase order and is used to calculate various performance metrics.

- `po_number`: Unique number identifying the PO.
- `vendor`: Link to the Vendor model.
- `order_date`: Date when the order was placed.
- `delivery_date`: Expected or actual delivery date of the order.
- `items`: Details of items ordered.
- `quantity`: Total quantity of items in the PO.
- `status`: Current status of the PO (e.g., pending, completed, canceled).
- `quality_rating`: Rating given to the vendor for this PO (nullable).
- `issue_date`: Timestamp when the PO was issued to the vendor.
- `acknowledgment_date`: Timestamp when the vendor acknowledged the PO.

### Historical Performance Model

The `HistoricalPerformance` model optionally stores historical data on vendor performance, enabling trend analysis.

- `vendor`: Link to the Vendor model.
- `date`: Date of the performance record.
- `on_time_delivery_rate`: Historical record of the on-time delivery rate.
- `quality_rating_avg`: Historical record of the quality rating average.
- `average_response_time`: Historical record of the average response time.
- `fulfillment_rate`: Historical record of the fulfilment rate.

## Backend Logic

The backend logic includes calculations for performance metrics:

- On-Time Delivery Rate
- Quality Rating Average
- Average Response Time
- Fulfilment Rate

## API Endpoint Implementation

- Vendor Performance Endpoint (GET /api/vendors/{vendor_id}/performance)
- Update Acknowledgment Endpoint (POST /api/purchase_orders/{po_id}/acknowledge)

## Technical Requirements

- Django: Latest stable version
- Django REST Framework: Latest stable version
- Adherence to RESTful principles in API design
- Django ORM for database interactions
- Token-based authentication
- PEP 8 style guidelines for Python code

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-vendor-management.git
    cd django-vendor-management
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser (optional):

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Contributing

We welcome contributions! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
