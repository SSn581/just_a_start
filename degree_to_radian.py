# for degrees to radian conversion
def deg_to_rad():
  pi=3.1415
  degree= float(input('Degrees: '))
  radian= degree*(pi/180)
  return radian
  
# for radian to degrees  
 def rad_to_deg():
   pi=3.1415
   radian= float(input('Radian: '))
   degree= radian*(180/pi)
   return degree

# main code  
if __name__=='__main__':
    print('Enter 1 for degree to radian convertion')
    print('Enter 2 for radian to degree convertion')
    choice= int(input('>'))
    if choice == 1:
        print(deg_to_rad())
    elif choice == 2:
        print(rad_to_deg())
        
print('finished')
