CREATE TABLE "staff" (
  "staff_id" integer PRIMARY KEY,
  "hiring_date" date,
  "department_id" integer,
  "role_type" varchar,
  "salary" decimal,
  "is_active" boolean DEFAULT true
);

CREATE TABLE "teacher" (
  "teacher_id" integer PRIMARY KEY,
  "staff_id" integer,
  "biography" text,
  "office_location" varchar,
  "academic_rank" varchar,
  "research_area" varchar
);

CREATE TABLE "student" (
  "student_id" integer PRIMARY KEY,
  "enrollment_date" date,
  "enrollment_status" varchar,
  "total_credits_earned" integer DEFAULT 0
);

CREATE TABLE "users" (
  "user_id" integer PRIMARY KEY,
  "first_name" varchar,
  "last_name" varchar,
  "date_of_birth" date,
  "email" varchar UNIQUE,
  "mobile" varchar,
  "tel" varchar,
  "address_line1" varchar,
  "address_line2" varchar,
  "city" varchar,
  "country" varchar,
  "postal_code" varchar
);

CREATE TABLE "course" (
  "course_id" integer PRIMARY KEY,
  "course_name" varchar,
  "description" text,
  "min_credits_required" integer,
  "base_tuition_fee" decimal
);

CREATE TABLE "module" (
  "module_id" integer PRIMARY KEY,
  "module_code" varchar UNIQUE,
  "title" varchar,
  "credits" integer,
  "syllabus" text,
  "teacher_id" integer
);

CREATE TABLE "course_modules" (
  "course_id" integer,
  "module_id" integer,
  "is_mandatory" boolean DEFAULT false,
  "primary" key(course_id,module_id)
);

CREATE TABLE "student_course_enrollment" (
  "enrollment_id" integer PRIMARY KEY,
  "student_id" integer,
  "course_id" integer,
  "start_date" date,
  "payment_status" varchar,
  "completion_date" date
);

CREATE TABLE "module_registration" (
  "registration_id" integer PRIMARY KEY,
  "enrollment_id" integer,
  "module_id" integer,
  "semester" varchar,
  "grade_achieved" decimal,
  "completion_date" date
);

CREATE TABLE "classroom" (
  "room_id" integer PRIMARY KEY,
  "virtual" bool,
  "room_name" varchar,
  "type" varchar,
  "capacity" integer,
  "location_details" varchar
);

CREATE TABLE "schedule" (
  "schedule_id" integer PRIMARY KEY,
  "module_id" integer,
  "room_id" integer,
  "day_of_week" varchar,
  "start_time" time,
  "end_time" time
);

CREATE TABLE "attendance" (
  "student_id" integer,
  "course_id" integer,
  "date" date,
  "presence" bool
);

CREATE TABLE "payments" (
  "payment_id" integer PRIMARY KEY,
  "enrollment_id" integer,
  "amount_paid" decimal,
  "payment_date" timestamp,
  "payment_method" varchar,
  "transaction_reference" varchar
);

ALTER TABLE "teacher" ADD FOREIGN KEY ("staff_id") REFERENCES "staff" ("staff_id");

ALTER TABLE "module" ADD FOREIGN KEY ("teacher_id") REFERENCES "teacher" ("teacher_id");

ALTER TABLE "course_modules" ADD FOREIGN KEY ("course_id") REFERENCES "course" ("course_id");

ALTER TABLE "course_modules" ADD FOREIGN KEY ("module_id") REFERENCES "module" ("module_id");

ALTER TABLE "student_course_enrollment" ADD FOREIGN KEY ("student_id") REFERENCES "student" ("student_id");

ALTER TABLE "student_course_enrollment" ADD FOREIGN KEY ("course_id") REFERENCES "course" ("course_id");

ALTER TABLE "module_registration" ADD FOREIGN KEY ("enrollment_id") REFERENCES "student_course_enrollment" ("enrollment_id");

ALTER TABLE "module_registration" ADD FOREIGN KEY ("module_id") REFERENCES "module" ("module_id");

ALTER TABLE "schedule" ADD FOREIGN KEY ("module_id") REFERENCES "module" ("module_id");

ALTER TABLE "schedule" ADD FOREIGN KEY ("room_id") REFERENCES "classroom" ("room_id");

ALTER TABLE "attendance" ADD FOREIGN KEY ("student_id") REFERENCES "student" ("student_id");

ALTER TABLE "attendance" ADD FOREIGN KEY ("course_id") REFERENCES "course" ("course_id");

ALTER TABLE "payments" ADD FOREIGN KEY ("enrollment_id") REFERENCES "student_course_enrollment" ("enrollment_id");

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "student" ("student_id");

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "teacher" ("teacher_id");

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "staff" ("staff_id");
