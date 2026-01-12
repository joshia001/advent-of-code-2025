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
            
            # only bother with ids that are of even length
            if len(id) % 2 != 0:
                continue
                        
            if id[:len(id)//2] == id[len(id)//2:]:
                # protect against duplicate or overlapping id ranges
                if id not in invalid_ids: 
                    invalid_ids.append(int(id))
                
    print(f'Sum of all invalid ids: {sum(invalid_ids)}')                
    
if __name__ == "__main__":
    main()
    