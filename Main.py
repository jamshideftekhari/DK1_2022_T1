from Repository import Repository

# Repository object instance
Repo = Repository()
# call setconnection metode to set connection to the database  
Repo.SetConnection()
# call Get all methode to fetch table elements and print on terminal/console 
Repo.GetAll()
# Add Row In the table
Repo.AddRow()
# Get all rows again 
Repo.GetAll()