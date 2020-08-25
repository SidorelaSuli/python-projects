# stores key-value pairs
# the keys are unique
monthConvertions = {
    "Jan" : "January",
    "Feb" : "Febuary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConvertions["Nov"])
print(monthConvertions.get("Dec"))
print(monthConvertions.get("one", "Not a valid key"))