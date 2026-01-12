import pandas as pd

def main():
    input_file_path = "day2\day2input.txt"
    id_ranges = pd.read_csv(input_file_path, sep=",", header=None)
    invalid_ids = []
    
    for id_range in id_ranges.values[0]:
        
        # Isolate start and stop integers from the 'id_range' string
        window = id_range.split("-")
        start = int(window[0])
        stop = int(window[1])
            
        for id in range(start, stop+1):
            
            id = str(id)
            
            substring = ''
            for i in range(len(id)//2):
                substring += id[i]
                
                if len(id) % len(substring) != 0:
                    continue
                
                # if id is a multiple of the substring, then it must be invalid
                if substring * (len(id) // len(substring)) == id:
                    if id not in invalid_ids:
                        invalid_ids.append(int(id))
                        break
                                                     
    print(f'Sum of all invalid ids: {sum(invalid_ids)}')                
    
if __name__ == "__main__":
    main()
    