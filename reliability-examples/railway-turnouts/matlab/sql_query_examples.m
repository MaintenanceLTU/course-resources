%% Create database connection parameters
user = "your_username";
password = "your_password";
host = "YOUR_VM_PUBLIC_IP";
dbname = "rail8";
port = 5432;

%% Connect to PostgreSQL
conn = postgresql(user, password, ...
    Server=host, DatabaseName=dbname, PortNumber=port);

%% BIS
% Return all turnout types
query = 'SELECT DISTINCT "Växeltyp" FROM bisdata;';

vxltyp = fetch(conn, query);
disp(vxltyp)

%% Close the connection when finished
close(conn)