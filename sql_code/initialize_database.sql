
CREATE DATABASE banking_system;

USE banking_system;


CREATE TABLE bank_user(
    id int,
    first_name varchar(255),
    last_name varchar(255),
    address varchar(255),
    primary key(id)
);

CREATE TABLE bank_account(
    id int,
    owner_id int NOT NULL,
    balance double,
    penalty_type_id int,
    
    primary key(id),
    foreign key(owner_id) references bank_user(id)
);

CREATE TABLE transactions(
    account_id int,
    transaction_date datetime,
	amount double,
    primary key(account_id, transaction_date),
    foreign key (account_id) references bank_account(id)
);


CREATE TABLE penalty(
    id int
);

