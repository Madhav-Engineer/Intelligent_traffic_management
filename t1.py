import time


def control_traffic_signal1(veh_count):
    lanes = ['lane 1', 'lane 2', 'lane 3', 'lane 4']
    lights = {'lane 1': 'G1', 'lane 2': 'G2', 'lane 3': 'G3', 'lane 4': 'G4'}
    cars1 = {}
    green_signal = []
    p=0

    count_list=veh_count
    # First data entry
    for lane in lanes:
        cars1[lane] = count_list[p]
        p=p+1
    max_cars1 = max(cars1.values())
    max_tie_lanes1 = [lane for lane, num_cars in cars1.items() if num_cars == max_cars1]
    green_signal.extend(max_tie_lanes1)
    for tie in max_tie_lanes1:
    # Print the traffic light status
     for lane in lanes:
        if(tie==lane):
         #if lane == max_lane:
            print(f"{ lights[tie]} on", end=' ') 
            #green_signal.extend(max_tie_lanes1)
        elif lane in cars1:  # Ensure the lane is still present in the dictionary
            print(f"R{lights[lane][1:]} on", end=' ')
            time.sleep(5)
     if(len(max_tie_lanes1)>1):
           print('\n')
           print(f"R{ lights[tie][1]} on")
        

    max_tie_lanes=max_tie_lanes1
    max_lane = max(cars1, key=cars1.get)
    '''
    max_light = lights[max_lane]
    for lane in lanes:
        if lane == max_lane:
            print(f"{max_light} on", end=' ')
        else:
            print(f"R{lights[lane][1:]} on", end=' ')'''
    print()

    time.sleep(5)
    return(max_tie_lanes,max_lane,cars1,lights,lanes,green_signal)
  
def control_traffic_signal2(veh_count,max_tie_lanes,max_lane,cars1,lights,lanes,green_signal):
    #while True:
      print('green_signal',green_signal)
      count_list=veh_count
      # Subsequent data entries
      for _ in range(1):
    
        # Remove the lane with the maximum number of cars from the input list
        #del cars[max_lane]
        cars=cars1.copy()
        #cars[max_tie_lanes[-1]]=0
        #cars[max_lane]=0
        #del lights[max_lane]
        
        # Ask for input for the remaining three lanes
        for lane in cars:
            if(cars[lane]==0):
                 continue
            p=int(lane[-1])-1
            #print(p)
            cars[lane] =count_list[p]
           
        # Find the lane with the maximum number of cars in the current entry
        if cars:
            #max_lane = max(cars, key=cars.get)
            #max_light = lights[max_lane]
            max_cars = max(cars.values())
            #print(cars)
            max_tie_lanes = [lane for lane, num_cars in cars.items() if num_cars == max_cars]
            green_signal.extend(max_tie_lanes)
            #print('max_tie_lanes', max_tie_lanes)
            for tie in max_tie_lanes:
                
            # Print the traffic light status
             for lane in lanes:
                if(tie==lane):
                 #if lane == max_lane:
                    print(f"{ lights[lane]} on", end=' ') 
                    
                    #green_signal.append(max_tie_lanes)
                elif lane in cars:  # Ensure the lane is still present in the dictionary
                    print(f"R{lights[lane][1:]} on", end=' ')
             if(len(max_tie_lanes)>1):
                   print('\n')
                   print(f"R{ lights[tie][1]} on")
                
        else:
            # If only one lane left, it gets the green light
            print(f"{lights[max_lane]} on", end=' ')
            

        print()

        time.sleep(5)
      for _ in range(3):
       p=False
       print('\n')
       
       for lane in lanes:
        
        if (lane not in green_signal) and (p==False):
           
           print(f"{ lights[lane]} on", end=' ')
           p=True
           green_signal.append(lane)
           #green_signal.append(max_tie_lanes)
        elif lane in cars:  # Ensure the lane is still present in the dictionary
           print(f"R{lights[lane][1:]} on", end=' ')
      green_signal.clear()