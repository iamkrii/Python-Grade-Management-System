import sqlite3
from sqlite3 import Connection, Error
from typing import List, Tuple, Union

from student import AssessmentType, StudentTuple, StudentWithMarks

def create_connection(db_file):
    """ Create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Successfully connected to {db_file}")
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def initialize_database():
    """ Initialize the database and create tables if they don't exist """
    database = r"grade_management.db"

    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        roll_number INTEGER PRIMARY KEY AUTOINCREMENT,
                                        student_name TEXT NOT NULL
                                    ); """

    # Updated marks table to include assessment_type
    sql_create_marks_table = """CREATE TABLE IF NOT EXISTS marks (
                                    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    roll_number INTEGER NOT NULL,
                                    assessment_type TEXT NOT NULL,
                                    marks REAL,
                                    FOREIGN KEY (roll_number) REFERENCES students (roll_number)
                                );"""

    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        # Create students table
        create_table(conn, sql_create_students_table)
        print("'students' table created or already exists.")

        # Create marks table
        create_table(conn, sql_create_marks_table)
        print("'marks' table created or already exists.")
        
        return conn
    else:
        print("Error! cannot create the database connection.")


def add_student_db(conn: Connection, student_name: str) -> Union[int, None]:
    sql = ''' INSERT INTO students(student_name)
              VALUES(?) '''
    cur = conn.cursor()
    try:
        # We pass a tuple with a single item (note the trailing comma)
        cur.execute(sql, (student_name,))
        conn.commit()
        
        # Get the roll_number of the last inserted row
        new_roll_number = cur.lastrowid
        
        return new_roll_number
    except sqlite3.Error as e:
        print(f"Error: Failed to add student. {e}")
        return None


def get_student_by_roll_db(conn: Connection, roll_number: int) -> Union[StudentTuple, None]:
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))

    # fetchone() retrieves the next row of a query result set.
    # It returns a single sequence, or None when no more data is available.
    student_data = cur.fetchone()

    return student_data

def add_grades_db(conn: Connection, roll_number: int, data: List[Tuple[AssessmentType, int]]) -> Union[str, None]:
    if not get_student_by_roll_db(conn, roll_number):
        return f"Student with roll number {roll_number} does not exist."

    sql = ''' INSERT INTO marks(roll_number, assessment_type, marks)
              VALUES(?,?,?) '''
    cur = conn.cursor()

    try:
        for assessment_type, marks in data:
            cur.execute(sql, (roll_number, assessment_type, marks))
        
        conn.commit()
        return None
    except sqlite3.Error as e:
        return f"Error adding grades: {e}"


def get_student_report_db(conn: Connection, roll_number: int) -> Union[List[StudentWithMarks], str]:
    sql = """
        SELECT
            s.roll_number,
            s.student_name,
            m.assessment_type,
            m.marks
        FROM
            students s
        LEFT JOIN
            marks m ON s.roll_number = m.roll_number
        WHERE
            s.roll_number = ?
        ORDER BY
            s.roll_number;
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, (roll_number,))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        return f"Error retrieving student: {e}"
    
    return rows


def get_total_students_count_db(conn: Connection) -> Union[int, str]:
    sql = "SELECT COUNT(*) FROM students;"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        count = cur.fetchone()[0]
        return count
    except sqlite3.Error as e:
        return f"Error retrieving student count: {e}"


def get_all_students_db(conn: Connection) -> Union[List[StudentWithMarks], str]:
    sql = """
        SELECT
            s.roll_number,
            s.student_name,
            m.assessment_type,
            m.marks
        FROM
            students s
        LEFT JOIN
            marks m ON s.roll_number = m.roll_number
        ORDER BY
            s.roll_number;
    """

    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        return f"Error retrieving students: {e}"
    
    return rows

def remove_student_db(conn: Connection, roll_number: int) -> Union[str, None]:    
    sql = "DELETE FROM students WHERE roll_number = ?"
    cur = conn.cursor()
    try:
        cur.execute(sql, (roll_number,))
        conn.commit()
        return None
    except sqlite3.Error as e:
        return f"Error removing student: {e}"