def main():
   #print the program name
   print("Calculating Time shift")
   print()
   #user inputs
   cur_time = input("Enter a time(hh:mm): ")
   cur_hours = int(cur_time.split(":")[0])
   cur_min = int(cur_time.split(":")[1])
   shift_mins = int(input("Enter a time shift in mins: "))
   
   #converting to minutes 
   total_cur_mins = (cur_hours * 60) + cur_min
   
   #calculate the time befor x min
   total_before_min = total_cur_mins - shift_mins
   before_hour = (total_before_min // 60) % 24
   before_min = (total_before_min % 60)
   
   print("Before: {:02d}:{:02d}".format(before_hour, before_min))
   
   # Calculate the time after x minutes
   total_after_min = total_cur_mins + shift_mins
   after_hour = (total_after_min// 60) % 24
   after_min = total_after_min % 60
   
   print("After: {:02d}:{:02d}".format(after_hour, after_min))

if __name__ == "__main__":
    main()