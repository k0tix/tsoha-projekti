# Documentation

## Use cases

An unregistered user can:
> * browse items that are on sale
> * create a user account

A registered user can:
> * browse items that are on sale
> * add own items for sale
> * buy items
> * modify the price of users own products that are on sale
> * add balance to account
> * bookmark items
> * remove bookmarks
> * name bookmarks

## Database diagram
![diagram](images/diagram2.png)

## CREATE TABLE:
### Item:
```sql
CREATE TABLE item (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        price INTEGER NOT NULL, 
        quality FLOAT NOT NULL, 
        item_type VARCHAR(144) NOT NULL, 
        sold BOOLEAN NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (sold IN (0, 1)), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```
* Item has a column sold, because every item is purchased only once and it would be unnecessary to go through all purchases when displaying an item

* Items type column is indexed so searching items by name and type will be significantly faster

### Account:
```sql
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        email VARCHAR(144) NOT NULL, 
        pwd_hash VARCHAR(144) NOT NULL, 
        balance INTEGER NOT NULL, 
        banned BOOLEAN NOT NULL, 
        role VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (banned IN (0, 1))
);
```

### Purchase:
```sql
CREATE TABLE purchase (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        account_id INTEGER NOT NULL, 
        item_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(item_id) REFERENCES item (id)
);
```

### Bookmark:
```sql
CREATE TABLE bookmark (
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144), 
        item_id INTEGER NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (item_id, account_id), 
        FOREIGN KEY(item_id) REFERENCES item (id), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```

## SQL-queries for different use cases

Browse items that are on sale:
```sql
SELECT Item.id, Item.name, Item.price, Item.quality, Item.item_type, Item.sold, Account.username FROM Item
    JOIN Account ON Account.id = Item.account_id
    WHERE Item.sold = FALSE;
```

Create a user account:
```sql
INSERT INTO Account(name, username, email, pwd_hash, balance, banned, role) VALUES(?,?,?,?,?,?,?);
```

Add own items for sale:
```sql
INSERT INTO Item(name, price, quality, item_type, sold) 
    VALUES("name", 20000, 0.234, "Common", FALSE);
```

Buy items:
```sql
INSERT INTO Purchase(account_id, item_id) VALUES(?,?);
```

Delete items:
```sql
DELETE FROM Item WHERE Item.id = ?
```

Add balance to account:
```sql
UPDATE Account
    SET balance = balance + 10000
    WHERE Account.id = ?;
```

Modify items:
```sql
UPDATE Item
    SET name="newname", price=12345, quality=0.345, item_type="Legendary", sold=FALSE
    WHERE Item.id = 1;
```

Bookmark items:
```sql
INSERT INTO Bookmark(account_id, item_id, name) VALUES(?, ?, "Best bookmark");
```

Update bookmark:
```sql
UPDATE Bookmark
    SET name="new name"
    WHERE Bookmark.account_id = ? AND Bookmark.item_id = ?;
```

Delete bookmark:
```sql
DELETE FROM Bookmark WHERE Bookmark.account_id = ? AND Bookmark.item_id = ?;
```