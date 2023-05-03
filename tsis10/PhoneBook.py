import psycopg2 
def create(): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        CREATE TABLE phonebook ( 
            id INTEGER PRIMARY KEY, 
            name VARCHAR(50), 
            last_name VARCHAR(50), 
            phone_number VARCHAR(50) 
        ); 
        ''') 
    conn.commit() 
    cur.close() 
 
 
def show(): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        SELECT * FROM phonebook;  
        ''') 
    conn.commit() 
    cur.close() 
 
      
 
def insert(id, name, lastName, phoneNumber): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        INSERT INTO phonebook ( 
            id,
            name, 
            last_name, 
            phone_number 
        ) 
        VALUES (%s, %s, %s, %s);
        ''', (id, name, lastName, phoneNumber)) 
    conn.commit() 
    cur.close() 
def upd(name, phoneNumber): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        UPDATE PhoneBook SET phone_number = %s WHERE name = %s;
        ''')
    conn.commit() 
    cur.close() 
def delete(name, phoneNumber): 
    conn = psycopg2.connect(database = 'pp2', user = 'postgres', password = '12345') 
    cur = conn.cursor() 
    cur.execute( 
        ''' 
        DELETE FROM PhoneBook WHERE name = %s;
        ''')
    conn.commit() 
    cur.close() 
 
def main(): 
    print('Your name:') 
    name = input() 
    print('Your last name:') 
    lastName = input() 
    print('Your phone number:') 
    phoneNumber = input() 
    insert(name, phoneNumber)