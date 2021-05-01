#!/bin/python3

import math
import os
import random
import re
import sys

# INCLUDE all functions from all previous PROBLEMS
#
#

#adt which creates register to store customer
def makeCustomerRegister():
    return ('CR', [])

#adt to get all customer information from the register
def contents(cr):
    return cr[1]

# checks if customer register was created by this program
def isCustomerRegister(cr):
    return type(cr) == type(()) and cr[0] == 'CR'

# checks if there are no customers currently registered
def isEmpty(cr):
    return contents(cr) == []

# adds customer record  to register
def addCustomer(custRec, cr):
    if isCustomerRegister(cr):
        contents(cr).append(custRec)
    else:
        raise TypeError('Needs to be a record')

# removes customer from register
def removeCustomer(cid, cr):
    if isCustomerRegister(cr) and not isEmpty(cr) :
        for record in contents(cr):
            if cid in record:
                contents(cr).remove(record)
    else:
        raise TypeError("Needs to be a record")


#gets customer first name's initial
def get_FInitial(name):
    return name[0][0].upper()
# get customer last name's initial 
def get_LInitial(name):
    return name[1][0].upper()

#get customer id
def get_CID(record):
    return record[0]

#generate a customer id
def generateCId(name,cr,platinum):
    if isCustomerRegister(cr) and type(name)==type(()) and type(platinum)==bool:
        ASCII= ord(get_FInitial(name)) + ord(get_LInitial(name))
        if platinum== True:
            mem_typ= "PC"
        else:
            mem_typ= "NC"

        CID = mem_typ + str(ASCII)
        for i in range(0,len(contents(cr))):            
            for record in contents(cr):        
                if CID in record:
                    ASCII +=1
                    CID = mem_typ + str(ASCII)
        return CID

# makes a customer record
def makeCustomerRecord(cid, hh, mm):
    return [cid, (hh,mm), str(-1), []]

# gets customer id from record
def getCID(custRec):
    return custRec[0]

#gets customer's arrival time at mechanic 
def getArivalTime(custRec):
    if (custRec[1][0])<10:
        return "0"+str(custRec[1][0])+str(custRec[1][1])
    else:
        return str(custRec[1][0])+str(custRec[1][1])

#gets the length of time taken to service vehicle 
def getServiceTime(custRec):
    return str(custRec[2])


#gets the type of customer Platinum or Normal
def getCustType(custRec):
    return getCID(custRec)[:2]

# gets the vehicle information from a crustomer record
def getVehicle(custRec):
    return custRec[3]

# update vehcile information
def updateVehicle(vhcl, custRec):
    custRec.pop()
    custRec.append(vhcl)

# update service time for a vehicle

def updateServiceTime(serviceTime, custRec):
    serve=getServiceTime(custRec)
    if serve == str(-1):
        custRec[2]=(serviceTime)
    else:
        custRect=str(int(custRec[2])+ int(serviceTime))
        
       
# updates the cost of the service for a vehicle   
def updateServiceCost(serviceCost,custRec):
    custRec[-1][-1] += serviceCost
    
# add vehicle inforation to a customer 
def addVehicle (CustomerRegister, CID, PL,Mk,Md,Y,Ml,LSD):
    for records in contents(CustomerRegister):
        if CID == get_CID(records):
            records.pop()
            records.append([PL, (Mk, Md, Y), Ml, LSD, 0])

#costs of varying vehicle 
servicing_cost_list = ("CL", (["Honda", (45000.00, "0230"), (10000.00, "0030"), (70000.00, "0130")],\
                             ["BMW", (90000.00, "0330"), (30000.00, "0040"), (16000.00, "0050")],\
                             ["Ferrari", (245000.5, "0650"), (100000.00, "0030"), (134000.00, "0130")],\
                             ["Toyota", (30000.00, "0130"), (10000.00, "0100"), (15000.00, "0040")],\
                             ["Suzuki", (25000.00, "0200"), (8000.00, "0035"), (11000.00, "0020")],\
                             ["Benz", (150000.00, "0435"), (67000.00, "0030"), (7800.00, "0030")]))


def svlContents(serv_lst):
    return serv_lst[1]

#get model of vehicle
def getMkSvl(serv_model):
    return serv_model[0]
  
#FH
def getFullHouseInfo(serv_lst,mk):
    for make in svlContents(serv_lst):
        if getMkSvl(make) == mk:
            return make[1]
# returns tyre information
def getTyreInfo(serv_lst,mk):
    for make in svlContents(serv_lst):
        if getMkSvl(make) == mk:
            return make[2]
#return information on the condition of vehicle shocks
def getShocksInfo(serv_lst,mk):
    for make in svlContents(serv_lst):
        if getMkSvl(make) == mk:
            return make[3]

# return the the cost of service    
def cost(activity_tuple):
    return activity_tuple[0]

# return estimated time of service
def estTime(activity_tuple):
    return activity_tuple[1]

# returns final cost of service
def getServCost(serv_lst,mk,activity):
    if activity == "FH":
        return cost(getFullHouseInfo(serv_lst,mk))
    elif activity == "SH":
        return cost(getShocksInfo(serv_lst,mk))
    elif activity == "TY":
        return cost(getTyreInfo(serv_lst,mk))

# return final time of service
def getActivTime(serv_lst,mk,activity):
    if activity == "FH":
        return estTime(getFullHouseInfo(serv_lst,mk))
    elif activity == "SH":
        return estTime(getShocksInfo(serv_lst,mk))
    elif activity == "TY":
        return estTime(getTyreInfo(serv_lst,mk))


# returns the max cost a customer can pay
def getPayLimit(vhcl): 
    return int(vhcl[0])

# return make of vehicle
def getMake(vhcl): 
    return vhcl[1][0]

#return model of vehicle
def getModel(vhcl): 
    return vhcl[1][1]

#return year of vehicle
def getYear(vhcl): 
    return int(vhcl[1][2])

# returns mileage 
def getMile(vhcl): 
    return int(vhcl[2])

# return last time vehicle was serviced
def getLastServDate(vhcl): 
    return int(vhcl[3])

# return cost of the service
def getSerVCost(vhcl):
    return float(vhcl[4])

# asseess Vehicle condition
def assessVehicle(CustomerRegister, CID, SCL):
    for customer in contents(CustomerRegister):
        if get_CID(customer)==CID:
            vehicle= getVehicle(customer)
            for servicing in svlContents(SCL):
                if getMkSvl(servicing)==getMake(vehicle):
                    
                    #PRELIMINARY ASSESMENT
                    
                    threshold= getPayLimit(vehicle)*1.05
                    fhc=getServCost(SCL,getMkSvl(servicing),'FH')
                    shc=getServCost(SCL,getMkSvl(servicing),'SH')
                    tyc=getServCost(SCL,getMkSvl(servicing),'TY')
                    prelim=[]
                    time=[]
                    updateServiceCost(0.0,customer)
                    #FULL ASSESSMENT 
                    
                    full_house_check= getMake(vehicle)!='Benz' and (2020-getYear(vehicle))>5
                    if full_house_check :
                        fht=getActivTime(SCL,getMkSvl(servicing),'FH')
                        updateServiceCost(round(fhc,1),customer)
                        time.append(int(fht))
                        prelim.append(fhc)
                        
                    if not full_house_check and getMile(vehicle)>100000:
                        sht=getActivTime(SCL,getMkSvl(servicing),'SH')                 
                        updateServiceCost(round(shc,1),customer)
                        #updateServiceTime(sht,customer)
                        time.append(int(sht))
                        prelim.append(shc)
                        
                    if getLastServDate(vehicle)>10:
                        tyt=getActivTime(SCL,getMkSvl(servicing),'TY')
                        updateServiceCost(round(tyc,1),customer)
                        #updateServiceTime(tyt,customer)
                        time.append(int(tyt))
                        prelim.append(tyc)                
                    # PAY LIMIT REDUCTION  
                    
                    prelim.sort()
                    while threshold<sum(prelim):
                        updateServiceCost(-(float(prelim.pop(0))),customer)
                    
                    ust=str(sum(time))
                    while  len(ust)<4:
                        ust='0'+ust
                        
                    a=int(ust[:-2])
                    b=int(ust[2:])
                    if a>=24:
                        a-=24
                    if b>=60:
                        a+=int(b/60)
                        b=(b%60)
                    shours=str(a)
                    smins=str(b)
                    if len(shours)<2:
                        shours='0'+shours
                    if len(smins)<2:
                        smins='0'+smins
                    finalserv=shours+smins
                    updateServiceTime(finalserv,customer)
                    
                    
                    #PICKUP TIME
                    
                    Arrival=(getArivalTime(customer))
                    ServiceTime=(getServiceTime(customer))
                    if int(ServiceTime)>0:
                        AHH=int(Arrival[:-2])
                        AMM=int(Arrival[2:])
                        SHH=int(ServiceTime[:-2])
                        SMM=int(ServiceTime[2:])

                        HH=AHH+int(SHH)
                        MM=(AMM+int(SMM))-5
                        if MM>=60:
                            HH+=int(MM/60)
                            MM=(MM%60)
                        if MM<0:
                            MM+=60
                            HH-=1
                        if HH>=24:
                            HH-=24
                        HH= str(HH)
                        MM=str(MM)
                        if len (HH)<2:
                            HH='0'+HH
                        if len(MM)<2:
                            MM='0'+MM
                        return HH+MM
                    else:
                        AHH=int(Arrival[:-2])
                        AMM=int(Arrival[2:])
                        HH=AHH
                        MM=AMM-5
                        if MM>=60:
                            HH+=int(MM/60)
                            MM=round(MM%60,2)
                        if MM<0:
                            MM+=60
                            HH-=1
                        if HH>=24:
                            HH-=24
                        HH= str(HH)
                        MM=str(MM)
                        if len (HH)<2:
                            HH='0'+HH
                        if len(MM)<2:
                            MM='0'+MM
                        return HH+MM
                    
# generates a queue for the order vehicles should be serviced                  
def makeServiceQ():
    return ("SQ", [])

# return the queue it self
def contentsQ(q):
    return q[1]

# returns vehicle at the front of the queue 
def frontServiceQ(q):
    if isServiceQ(q):
        return contentsQ(q)[0]
    else:
        raise TypeError("Needs to be a queue")
# adds vehicle to the queue
def addToServiceQ(custRec,q):

    def getInsertPos(CusType,arivalTime,lst):

        if lst == []:

            return 0

        else:

            if (getCustType(lst[0]) == CusType):

                if (int(getArivalTime(lst[0])) <= arivalTime):

                    return 1 + getInsertPos(CusType,arivalTime,lst[1:])

                else:

                    return getInsertPos(CusType,arivalTime,lst[1:])

            else:

                if (getCustType(lst[0]) == "PC" and CusType == "NC"):

                    return 1 + getInsertPos(CusType,arivalTime,lst[1:])

                else:

                    return getInsertPos(CusType,arivalTime,lst[1:])



    CusType = getCustType(custRec)

    arivalTime = int(getArivalTime(custRec))

    part = 7

    if part <= 6:

        contentsQ(q).append(custRec)

    else:

        contentsQ(q).insert(getInsertPos(CusType,arivalTime,contents(q)),custRec)
# remove vehcile from queue 
def removeFromServiceQ(q):
    if isServiceQ(q)and not isEmptyServiceQ (q):
        contents(q).pop(0)
# checks if queue was created by program
def isServiceQ(q):
    return type(q)==type(()) and q[0]== "SQ" and type(contentsQ(q))==type([]) and len(q)==2
# checks if queue is empty
def isEmptyServiceQ (q):
    return isServiceQ(q) and contentsQ(q)==[]

# returns customer information for car in queue 
def getCustRec(CustomerRegister,CID):
    for custRec in contents(CustomerRegister):
        if getCID(custRec) == CID:
            return custRec
    return -1

# creates a stack for vehicles which which has been serviced and needs to be picked up   
def makePickupStack():
    return ('VP',[])

# retuns the stack itself
def contentsStack(st):
        return st[1]

# retuns vehicle at the top of the stack
def topPickupStack(st):
    if isVPstack(st):
        return contentsStack(st)[0]
    else:
        raise TypeError ('Needs to be a stack')
    
# adds a vehcile to the the top of the stack
def pushPickupStack(custRec,st):
    if isVPstack(st):
        contentsStack(st).insert(0,getCID(custRec))
    else:
        raise TypeError ('Needs to be a stack')
# removes vehciles from the top of the stack   
def popPickupStack(st):
    if isVPstack(st) and not isEmptyPickupStack(st):
        contentsStack(st).pop(0)
    else:
        raise TypeError ('Needs to be a stack and have elements in it')
# checks if it is a stack    
def isVPstack(st):
    return type(st)==type(()) and type(contentsStack(st))==type([]) 
# checks if there s  no car to be picked up
def isEmptyPickupStack(st):
    return contentsStack(st)==[]

#
#Part 7 – Serve The Customer
#

# return time serivce was completed
def get_completion_time(at,st,start):
    at = max(at,start)
    at_hh = at[:2]
    at_mm = at[2:]
    st_hh = st[:2]
    st_mm = st[2:]
    pt_hhi = int(at_hh)+int(st_hh)
    pt_mmi = int(at_mm)+int(st_mm)
    if pt_mmi > 59:
        pt_hhi += 1
        pt_mmi -= 60
    if pt_hhi > 23:
        pt_hhi -= 24
    pt = str(pt_hhi).zfill(2) + str(pt_mmi).zfill(2)
    return pt

# sorts customers queue and pickup stack
def serveCust(CustomerRegister,ServiceQueue,VehiclePickupStack):
    
    def sortCR(customerLst):
        sortedCR = [customerLst[0]]
        for custRec in customerLst[1:]:
            i = 0
            while getArivalTime(custRec) >= getArivalTime(sortedCR[i]):
                i += 1
                if i == len(sortedCR):
                    break
            sortedCR.insert(i, custRec)
        return sortedCR
    
    if not isEmpty(CustomerRegister):
        total_serv_hh, total_serv_mm, total_elap_hh, total_elap_mm = 0, 0, 0, 0
        sortedCustomerRegister = sortCR(contents(CustomerRegister))
        start_time = getArivalTime(sortedCustomerRegister[0])
        vPS = contentsStack(VehiclePickupStack)
        vSL = [getCID(c) for c in vehicleServList]
        for custRec in sortedCustomerRegister:
            if not isEmptyServiceQ(ServiceQueue):
                while get_completion_time(getArivalTime(frontServiceQ(ServiceQueue)), \
                                getServiceTime(frontServiceQ(ServiceQueue)), \
                                start_time) \
                            <= getArivalTime(custRec):
                    if getCID(frontServiceQ(ServiceQueue)) not in vPS+vSL:
                        pushPickupStack(frontServiceQ(ServiceQueue), VehiclePickupStack)
                    total_serv_hh += int(getServiceTime(frontServiceQ(ServiceQueue))[:2])
                    total_serv_mm += int(getServiceTime(frontServiceQ(ServiceQueue))[2:])
                    total_elap_hh += int(getServiceTime(frontServiceQ(ServiceQueue))[:2])
                    total_elap_mm += int(getServiceTime(frontServiceQ(ServiceQueue))[2:])
                    if start_time > getArivalTime(frontServiceQ(ServiceQueue)):
                        st_hh = int(start_time) // 100 + int(getServiceTime(frontServiceQ(ServiceQueue))[:2])
                        st_mm = int(start_time) % 100 + int(getServiceTime(frontServiceQ(ServiceQueue))[2:])
                        st_hh += st_mm // 60
                        st_mm = st_mm % 60
                        start_time = str(st_hh * 100 + st_mm).zfill(4)
                    else:
                        hh_diff = int(getArivalTime(frontServiceQ(ServiceQueue))[:2]) - \
                                     int(start_time[:2])
                        mm_diff = int(getArivalTime(frontServiceQ(ServiceQueue))[2:]) - \
                                     int(start_time[2:])
                        start_time = get_completion_time(getArivalTime(frontServiceQ(ServiceQueue)), \
                                        getServiceTime(frontServiceQ(ServiceQueue)), \
                                        start_time)
                        total_elap_hh += hh_diff
                        total_elap_mm += mm_diff
                    removeFromServiceQ(ServiceQueue)

                    if isEmptyServiceQ(ServiceQueue):
                        break
            if getCID(custRec) not in map(getCID, contentsQ(ServiceQueue)):
                addToServiceQ(custRec,ServiceQueue)
        part = 8
        if part <= 7:
            while not isEmptyServiceQ(ServiceQueue):
                pushPickupStack(frontServiceQ(ServiceQueue), VehiclePickupStack)
                total_serv_hh += int(getServiceTime(frontServiceQ(ServiceQueue))[:2])
                total_serv_mm += int(getServiceTime(frontServiceQ(ServiceQueue))[2:])
                total_elap_hh += int(getServiceTime(frontServiceQ(ServiceQueue))[:2])
                total_elap_mm += int(getServiceTime(frontServiceQ(ServiceQueue))[2:])
                if start_time > getArivalTime(frontServiceQ(ServiceQueue)):
                    st_hh = int(start_time) // 100 + int(getServiceTime(frontServiceQ(ServiceQueue))[:2])
                    st_mm = int(start_time) % 100 + int(getServiceTime(frontServiceQ(ServiceQueue))[2:])
                    st_hh += st_mm // 60
                    st_mm = st_mm % 60
                    start_time = str(st_hh * 100 + st_mm).zfill(4)
                else:
                    hh_diff = int(getArivalTime(frontServiceQ(ServiceQueue))[:2]) - \
                                 int(start_time[:2])
                    mm_diff = int(getArivalTime(frontServiceQ(ServiceQueue))[2:]) - \
                                 int(start_time[2:])
                    start_time = get_completion_time(getArivalTime(frontServiceQ(ServiceQueue)), \
                                    getServiceTime(frontServiceQ(ServiceQueue)), \
                                    start_time)
                    total_elap_hh += hh_diff
                    total_elap_mm += mm_diff
                removeFromServiceQ(ServiceQueue)

        total_serv_hh += total_serv_mm // 60
        total_serv_mm = total_serv_mm % 60
        total_elap_hh += total_elap_mm // 60
        total_elap_mm = total_elap_mm % 60
        remainingS_hh = 23 - total_serv_hh
        remainingS_mm = 60 - total_serv_mm
        remainingE_hh = 23 - total_elap_hh
        remainingE_mm = 60 - total_elap_mm
        if remainingS_mm > 59:
            remainingS_hh += 1
            remainingS_mm -= 60
        remainingS = remainingS_hh * 100 + remainingS_mm
        if remainingE_mm > 59:
            remainingE_hh += 1
            remainingE_mm -= 60
        remainingE = remainingE_hh * 100 + remainingE_mm
        if total_elap_hh > 23:
            return 0
        else:
            return remainingE
    else:
        return 2400

# removes customer from waiting list and vehicle from pick up stack
def pickupVehicle(CID,wlist,pickup_stack):
    make= getMake(getVehicle(getCustRec(custReg,CID)))
    model=getModel(getVehicle(getCustRec(custReg,CID)))
    year=getYear(getVehicle(getCustRec(custReg,CID)))
    
    
    if isEmptyPickupStack(pickup_stack):
        return (CID,'','','')
    if CID == topPickupStack(pickup_stack):
        popPickupStack(pickup_stack)
        return (CID,make,model,year)
    else:
        wlist.append(CID)
        return (CID,'','','')
# generates an interface to input customer information 
def service():
    def getcustfname(lst):
        return lst[0]
    def getcustlname(lst):
        return lst[1]
    def getA_H(lst):
        return lst[2]
    def getA_M(lst):
        return lst[3]
    
    yn=(input('Enter "Y" or "N" if there is a vehicle to be serviced : '))
    while yn=='Y':
        if yn=='Y':
            cust_info=input('\nEnter Customer First Name,Customer Last Name,24-Hr Arrival Hour,24-Hr Arrival Minutes: ')
            cust_info=cust_info.split()
            temp_cidPC=generateCId((cust_info[0],cust_info[1]),custReg,True)
            temp_cidNC=generateCId((cust_info[0],cust_info[1]),custReg,False)
            
        
        
            for cidcheck in contents(custReg):
                if temp_cidPC==getCID(cidcheck):
                    pickupVehicle(temp_cid,waitinglist,pickupStack)
                elif temp_cidNC in custReg:
                    pickupVehicle(temp_cid,waitinglist,pickupStack)
                else:
                    cus_type=input('\nDoes the Customer desire to be a Platinum Customer [Y/N] : ')
                if cus_type=='Y':
                    cus_type=True
                    cid=temp_cidPC
                else:
                    cus_type=False
                    cid=temp_cidNC
                pay_l=input('\nEnter the most the customer can afford for servicing the vehicle : ')
                MMY=input('\nEnter the make model and year of the vehicle : ')
                MMY=MMY.split()
                def m_ake(lst):
                    return lst[0]
                def m_odel(lst):
                    return lst[1]
                def y_ear(lst):
                    return lst[2]
            
                mil=input('\nEnter the current mileage on the vehicle : ')
                lsd=int(input('\nEnter the Last Service Date of the vehicle : '))
            
                new_cust=makeCustomerRecord(cid, int(getA_H(cust_info)), int(getA_M(cust_info)))
                addCustomer(new_cust,custReg)
                addVehicle (custReg,cid,pay_l,m_ake(MMY),m_odel(MMY),y_ear(MMY),mil,lsd)
                assessVehicle(custReg,cid,servicing_cost_list)
                serveCust(custReg,serviceQueue,pickupStack)
            
            y=getYear(getVehicle(new_cust))
            ma=getMake(getVehicle(new_cust))
            mo=getModel(getVehicle(new_cust))
        
        
            print('\nCID -',cid+', ',str(y)+',' , ma+',' ,mo+'; ' ,'Estimated Pickup Time :',\
                  assessVehicle(custReg,cid,servicing_cost_list))
            x=('\nCID -',cid+', ',str(y)+',' , ma+',' ,mo+'; ' ,'Estimated Pickup Time :',\
                  assessVehicle(custReg,cid,servicing_cost_list))
            
            
                
                

        yn=(input('\n\nEnter "Y" or "N" if there is a vehicle to be serviced : '))
    
            

