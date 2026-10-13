data_1d = []
data_2d = []

data_summary = {
    "total_values": 0,
    "min_value": None,
    "max_value": None,
    "sum_of_values": 0,
    "mean_value": 0.0,
}

def update_data_summary(summary):
    """Updates the summary with the latest data values."""
    
    global data_summary
    
    if not summary:
        data_summary = {"total_values": 0,"min_value": None,"max_value": None,"sum_of_values": 0,"mean_value": 0.0}
        return

    data_summary["total_values"] = len(summary)
    data_summary["min_value"] = min(summary)
    data_summary["max_value"] = max(summary)
    data_summary["sum_of_values"] = sum(summary)
    data_summary["mean_value"] = sum(summary) / len(summary)
    
def input_data():
    """Takes input from the user and stores it in a list or matrix."""

    
    global data_1d, data_2d
    
    print("\n","="*20,"Input data","="*20)
    print("1. Enter 1D array manually (space-separated integers)")
    print("2. Enter 2D array (nested list) manually")
    
    choice = input("Please enter your choice (1-2): ").strip()
    
    if choice == "1":
        user_data = input("Enter a data for 1D array (separated by spaces): ")
        data_1d = []
        for x in user_data.split():
            data_1d.append(int(x))
        update_data_summary(data_1d)
        print("1D array stored succesfully.")
        
    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        data_2d = []
        
        for i in range(rows):
            row_input = input(f"Enter row {i+1} values (separated by spaces): ")
            row_list = []
            for x in row_input.split():
                row_list.append(int(x))
            data_2d.append(row_list)
            
        matrix = []
        for row in data_2d:
            for item in row:
                matrix.append(item)
        
        update_data_summary(matrix)
        print("2D array stored successfully.")
    else:
        print("Invalid choice.")
        

def display_data_summary():
    """Displays the total, minimum, maximum, sum, and average of the data."""
    print(display_data_summary.__doc__)
    
    print("\nSelect Data to Summarize:")
    print("1. 1D Data")
    print("2. 2D Data")
    choice = input("Enter your choice (1-2): ").strip()
    
    if choice == "1":
        if len(data_1d) == 0:
            print("Data is not available in 1d array so input a data by option 1.")
            return
        data = data_1d
        print("\n1D Data:", data_1d)
    
    elif choice == "2":
        if len(data_2d)== 0:
            print("Data is not available in 2d array so input a data by option 1.")
            return
        print("\n2D Array Structure:")
        for row in data_2d:
            print(row)
            data = []
            for row in data_2d:
                for item in row:
                    data.append(item)
    
    else:
        print("Invaild choice.")
        return
        
    print("\nData Summary:")
    print(f"~ Total values: {len(data)}")
    print(f"~ Minimum values: {min(data)}")
    print(f"~ Maximum values: {max(data)}")
    print(f"~ Sum of all values: {sum(data)}")
    print(f"~ Average values: {sum(data) / len(data):.2f}")
    
    
def factorial(num):
    """Finds the factorial of a number using recursion."""
    if num < 0:
        return "Invalid number"
    if num==1 or num==0:
        return 1
    return num * factorial(num - 1)

    

def filter_data_by_threshold():
    """Filters the data and shows values greater than or equal to the given number."""
    print(filter_data_by_threshold.__doc__)
    
    print("\nSelect Data to Filter:")
    print("1. 1D Data")
    print("2. 2D Data")
    choice = input("Enter your choice (1-2): ").strip()
    
    data = []
    if choice == "1":
        if len(data_1d) == 0:
            print("No 1D data is available.")
            return
        data = data_1d
    elif choice == "2":
        if len(data_2d) == 0:
            print("No 2D data is available.")
            return
        for row in  data_2d:
            for item in row:
                data.append(item)
    else:
        print("Invalid Choice.")
            
        
    threshold = int(input("Enter a  threshold value to filter out data above this value: "))
    filter_data =  list(filter(lambda x: x>=threshold, data))
    print(f"Filtered Data (values >= {threshold}):")
    print(", ".join(map(str, filter_data)))
    
def sort_data():
    """Sorts the data in ascending or descending order."""

    print(sort_data.__doc__)
    
    print("\nSelect Data to Sort:")
    print("1. 1D Data")
    print("2. 2D Data (Sort rows)")
    choice = input("Enter your choice (1-2): ").strip()
    
    if choice == "1":
        if len(data_1d)==0:
            print("No 1d Data Available.")
        print("Choose sorting option:") 
        print("1. Ascending")
        print("2. Descending")
        option = input("Enter yotur choice: ").strip() 
        
        if option == "1":
            sorted_list = sorted(data_1d)
            print("Sorted Data in Ascending Order:")
            print(", ".join(map(str, sorted_list)))
        elif option == "2":
            sorted_list = sorted(data_1d, reverse=True)
            print("Sorted data in Descending Order:")
            print(", ".join(map(str, sorted_list)))
        else:
            print("Invalid choice.")
            
    elif choice== "2":
        if len(data_2d) ==0:
            print("No 2d Data Available.")
            return
        print("Sorting row in 2D list (using sorted()):")
        sorted_2d = []
        for row in data_2d:
            sorted_2d.append(sorted(row))
        for row in sorted_2d:
            print(row)
            
            
def display_dataset_statistics():
    """Displays dataset statistics about the data."""
    print(display_dataset_statistics.__doc__)
    
    print("\nSelect Data for Statistics:")
    print("1. 1D Data")
    print("2. 2D Data")
    choice = input("Enter your choice (1-2): ").strip()
    
    data = []
    if choice == "1":
        if len(data_1d) == 0:
            print("No 1d data available.")
            return
        data = data_1d 
    elif choice == "2":
        if  len(data_2d) == 0:
            print("No 2d data available") 
        for row in data_2d:
             for item in row:
                 data.append(item)
    
    else:
        print("Invalid choice.")
        return
    
    def get_statistics(nums):
        minimum = min(nums)   
        maximum = max(nums) 
        total = sum(nums)
        avg = total / len(nums)
        return minimum,maximum,total,avg        

    min_value,max_value,total_value,average_value = get_statistics(data)
    print("\nDataset Statistics:")
    print(f"~ Minimum value: {min_value}")
    print(f"~ Maximun value: {max_value}")
    print(f"~ total value: {total_value}")
    print(f"~ Average value: {average_value:.2f}")
    

def demo_args(*args):
    """Shows how to pass multiple values using *args."""
    print(demo_args.__doc__)
    for arg in args:
        print(f"~ {arg}")
        
def demo_kwargs(**kwargs):
    """Shows how to pass named values using **kwargs."""
    print(demo_kwargs.__doc__)
    for key, value in kwargs.items():
        print(f"~ {key}: {value}")
        
while True:
    print("\n","="*20,"Welcome to the Data Analyzer and Transformer Program","="*20)
    print("Main Menu:")
    print("1. Input Data (1D or 2D)")
    print("2. Display Data Summary (Built-in functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. *args Demo")
    print("8. **kwargs Demo")
    print("9. Exit Program")        
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        input_data()
    elif choice == "2":
        display_data_summary()
    elif choice == "3":
        print(factorial.__doc__)
        num = int(input("Enter a number:"))
        result = factorial(num)
        print(f"Fectorial {num} is {result}")
    elif choice == "4":
        filter_data_by_threshold()
    elif choice == "5":
        sort_data()
    elif choice == "6":
        display_dataset_statistics()
    elif choice == "7":
        demo_args(20,50,30,16,79)
    elif choice == "8":
        data_count = 0
        if data_2d:
            for row in data_2d:
                for item in row:
                    data_count += 1
        
        else:
            data_count = len(data_1d)
            
        if data_2d:
            dataset_type = "2D Matrix"
        else:
            dataset_type = "1D List"

        demo_kwargs(
            Dataset_Type=dataset_type,
            Element_Count=data_count
        )
    
    elif choice == "9":
        print("\nThank you.")
        exit()
    else:
        print("Invalid Choice. Please enter a number between 1 and 9.")
        
    



    

    