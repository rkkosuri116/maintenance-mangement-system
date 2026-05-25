from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="maintenance_user",
    password="admin123",
    database="maintenance_system"
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        machine_name = request.form['machine_name']
        location = request.form['location']
        status = request.form['status']
        install_date = request.form['install_date']

        query = """
        INSERT INTO machines
        (machine_name, location, status, install_date)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            machine_name,
            location,
            status,
            install_date
        )

        cursor.execute(query, values)

        db.commit()

        return redirect('/')

    cursor.execute("SELECT * FROM machines")

    machines = cursor.fetchall()

    return render_template(
        'index.html',
        machines=machines
    )

@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():

    if request.method == 'POST':

        machine_id = request.form['machine_id']
        maintenance_date = request.form['maintenance_date']
        issue_description = request.form['issue_description']
        technician_name = request.form['technician_name']
        downtime_minutes = request.form['downtime_minutes']

        query = """
        INSERT INTO maintenance_logs
        (
            machine_id,
            maintenance_date,
            issue_description,
            technician_name,
            downtime_minutes
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            machine_id,
            maintenance_date,
            issue_description,
            technician_name,
            downtime_minutes
        )

        cursor.execute(query, values)

        db.commit()

        return redirect('/maintenance')

    cursor.execute("SELECT * FROM machines")

    machines = cursor.fetchall()

    cursor.execute("""
        SELECT
            maintenance_logs.log_id,
            machines.machine_name,
            maintenance_logs.maintenance_date,
            maintenance_logs.issue_description,
            maintenance_logs.technician_name,
            maintenance_logs.downtime_minutes
        FROM maintenance_logs
        JOIN machines
        ON maintenance_logs.machine_id = machines.machine_id
    """)

    logs = cursor.fetchall()

    return render_template(
        'maintenance.html',
        machines=machines,
        logs=logs
    )

@app.route('/dashboard')
def dashboard():

    # Total Machines

    cursor.execute(
        "SELECT COUNT(*) FROM machines"
    )

    total_machines = cursor.fetchone()[0]

    # Total Maintenance Logs

    cursor.execute(
        "SELECT COUNT(*) FROM maintenance_logs"
    )

    total_logs = cursor.fetchone()[0]

    # Total Downtime

    cursor.execute(
        "SELECT SUM(downtime_minutes) FROM maintenance_logs"
    )

    total_downtime = cursor.fetchone()[0]

    # Most Problematic Machine

    cursor.execute("""
        SELECT
            machines.machine_name,
            SUM(maintenance_logs.downtime_minutes)
            AS total_downtime
        FROM maintenance_logs
        JOIN machines
        ON machines.machine_id = maintenance_logs.machine_id
        GROUP BY machines.machine_name
        ORDER BY total_downtime DESC
        LIMIT 1
    """)

    problematic_machine = cursor.fetchone()

    return render_template(
        'dashboard.html',
        total_machines=total_machines,
        total_logs=total_logs,
        total_downtime=total_downtime,
        problematic_machine=problematic_machine
    )

@app.route('/delete_machine/<int:id>')
def delete_machine(id):

    query = "DELETE FROM machines WHERE machine_id = %s"

    cursor.execute(query, (id,))

    db.commit()

    return redirect('/')

@app.route('/delete_log/<int:id>')
def delete_log(id):

    query = "DELETE FROM maintenance_logs WHERE log_id = %s"

    cursor.execute(query, (id,))

    db.commit()

    return redirect('/maintenance')

if __name__ == '__main__':
    app.run(debug=True)