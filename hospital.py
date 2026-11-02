
from mysql import connector


class HospitalManager:

    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Aswin@2005",
            database="hospital_db"
        )
        print("connected successfully")

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "select * from patient where id=%s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)
            return None

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
            insert into patient
            (name, age, gender, mobile, place,
            disease, doctor, appointment_date)
            values(%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)

            self.connection.commit()

            print("patient added successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "select * from patient"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            return records

        except Exception as e:
            print(e)
            return []

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)

            if record == None:
                print("patient not found")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record != None:

                self.cursor = self.connection.cursor()

                query = "delete from patient where id=%s"
                values = (id,)

                self.cursor.execute(query, values)

                self.connection.commit()

                print("patient deleted successfully..!")

            else:
                print("patient not found")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:

                allowed_columns = [
                    "name", "age", "gender", "mobile",
                    "place", "disease", "doctor",
                    "appointment_date"
                ]

                if not kwargs or any(
                    k not in allowed_columns for k in kwargs
                ):
                    print("Invalid update details")
                    return

                self.cursor = self.connection.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s, "

                placeholder = placeholder.rstrip(", ")

                query = f"update patient set {placeholder} where id=%s"

                values = [v for v in kwargs.values()]

                values.append(id)

                self.cursor.execute(query, values)

                self.connection.commit()

                print("patient details updated successfully")

            else:
                print("patient not found..")

        except Exception as e:
            print(e)


patient_instance = HospitalManager()

patient_instance.get()

print("_____details of one patient_____")
patient_instance.retrieve(id=1)

print("_____delete operation_____")
# patient_instance.delete(id=1)

print("_____after updation_____")
# patient_instance.put(2, place="Kannur")

patient_instance.get()
