readinteger <- function()
{ 
  n <- readline(prompt="Enter a year: ")
  if(!grepl("^[0-9]+$",n))
  {
    return(readinteger())
  }
  
  return(as.integer(n))
}

year = readinteger()

if (year%%4 == 0){
  print("Leap year.")
}else{
  print("Not a leap year.")
}