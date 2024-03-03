print("What's your name?")
recipient_name = input()
print("What year were you born?")
birth_year = int(input())
current_year = 2024
age =(current_year - birth_year)
message = "This is an arbitrary Birthday message."
sender_name = "Wellwisher"
print("Dear {}, let's celebrate your {} years of awesomeness!" .format(recipient_name, age))
print("Wishing you a day filled with joy and laughter as you turn {}." .format(age))
print(message)
print("With love and best wishes,")
print(sender_name)

