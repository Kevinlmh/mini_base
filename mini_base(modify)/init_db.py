# init_db.py
import schema_db
import storage_db

def init_database():
    # 初始化schema
    schema = schema_db.Schema()

    # 创建student表
    student_fields = [
        ("s_id", 0, 10),   # str类型，长度10
        ("name", 0, 50),    # str类型，长度50
        ("gender", 0, 10),  # str类型，长度10
        ("age", 2, 4)       # int类型
    ]
    schema.appendTable("student", student_fields)

    # 创建course表
    course_fields = [
        ("c_id", 0, 10),     # str类型，长度10
        ("title", 0, 100),    # str类型，长度100
        ("semester", 0, 20),  # str类型，长度20
        ("credit", 2, 4)      # int类型
    ]
    schema.appendTable("course", course_fields)

    # 创建takes表
    takes_fields = [
        ("s_id", 0, 10),   # str类型，长度10
        ("c_id", 0, 10),    # str类型，长度10
        ("score", 2, 4)     # int类型
    ]
    schema.appendTable("takes", takes_fields)

    # 插入student数据
    student_data = storage_db.Storage("student")
    student_data.insert_record(["s01", "Tom", "male", "19"])
    student_data.insert_record(["s02", "Jack", "male", "20"])
    student_data.insert_record(["s03", "Lily", "female", "17"])
    del student_data

    # 插入course数据
    course_data = storage_db.Storage("course")
    course_data.insert_record(["c01", "database system", "fall", "3"])
    course_data.insert_record(["c02", "web", "spring", "2"])
    del course_data

    # 插入takes数据
    takes_data = storage_db.Storage("takes")
    takes_data.insert_record(["s01", "c02", "90"])
    takes_data.insert_record(["s02", "c01", "89"])
    takes_data.insert_record(["s01", "c02", "49"])
    del takes_data

    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()