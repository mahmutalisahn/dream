## This is backend API project

# Used Technologies

 * Python
 * FastAPI
 * PostgreSQL
 * SQLAlchemy
 * Deta

# What's inside ?

* There are different types of endpoints in this project.

* There different types of sql operation in this project. You can see the different usage of SQLAlchemy.

# How to start ?

* You first need to clone this repository.

* After cloning, you need to create a postgresql server, here are the queries you need to create tables.

<br>

```sql
create table public.bookings
(
    booking_id       varchar,
    user_id          varchar,
    customer_email   varchar,
    customer_name    varchar,
    customer_surname varchar,
    customer_phone   varchar,
    start_book       time,
    end_book         time,
    date             date,
    status           integer,
    service_id       varchar
);
```

```sql
create table public.calendar
(
    user_id   varchar,
    monday    varchar,
    tuesday   varchar,
    wednesday varchar,
    thursday  varchar,
    friday    varchar,
    saturday  varchar,
    sunday    varchar
);
```

```sql
create table public.service
(
    service_id          varchar,
    user_id             varchar,
    service_name        varchar,
    service_description varchar,
    service_price       integer,
    service_duration    integer
);
```

```sql
create table public.user
(
    ssn      varchar,
    user_id  varchar,
    email    varchar,
    username varchar,
    password varchar,
    name     varchar,
    surname  varchar,
    phone    varchar
);
```

* After creating these tables in your database, configure .env.example file.
* run  ` uvicorn main:app --reload --host=0.0.0.0 ` inside of the project file, otherwise you may have import problems.
* type `http://0.0.0.0:8000/v1/editor_backend/docs#/default` to your web browser.

Thank you.
