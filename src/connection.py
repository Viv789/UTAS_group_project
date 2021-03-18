import psycopg2
conn = psycopg2.connect(
    host="de-redshift-redshiftcluster-9f0b8raon4t4.cwuax6l0wxln.eu-west-1.redshift.amazonaws.com", database="dev5", user="awsuser", password="InsecurePassword1234!", port=5439)
mycursor = conn.cursor()