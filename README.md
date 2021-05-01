# COMP1127_Project
 The purpose of the program is to create a customer service system which handles vehicle servicing for a generic car dealership.
 
This program has the ability to create a customer register to store  customer's personal and vehicle information for servicing 

It also handles generating the cost of servicing, based off  some key factors that will affect the price of the service. The customer would have already indicated what the limit is that they are willing to pay (Pay Limit - PL). If the cost of the servicing goes over that limit by more than 5%, the assessment cost the program should make a note on the register but remove the lowest costs from the list until it is within that 5% threshold.

There is a servicing cost list which denotes the general cost for certain tasks or jobs to be done on a vehicle based on the make (MK) of the vehicle. The servicing cost list is of the format: 

Mk – Make of Vehicle
FH – Full house check cost (float)
TC – Tyre Change cost (float)
ShT – shocks test cost (float)
ET – Estimated time for the service activity.

Other factors which affect cost:
If the vehicle is more than five years old and the make (Mk) is not a Benz, then the mechanic will have to do a full house check.
A mileage over 100,000 will incur a shocks test if a full house is not being done.
Tyres will need to be changed if the last service date is more than 10 months ago.

The program also has the ability to generate a queue for vehicles to be serviced and a stack for the vehcile to be picked up from. 

Customers are also seperated by type either Platinum or Normal
