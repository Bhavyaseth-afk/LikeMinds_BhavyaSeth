# role based

# read and write
# image also but user will create it
class RBAC():
    access=['read','write']

    user=['user1','user2']

    roles=['role1']

    resource=[]
    
    
    access_dic={}
    for i in user:
        if access_dic[i] not in access_dic:
            access_dic[i]=[roles[i]]
        else:
            access_dic[i].append(roles[i])

        # user1:[role1,admin,usernot]
        # user2:[role2] 

    def __init__(self,name,role):
        self.name=name
        self.role=role

    def addAccess(self,file):
        # read and write
        
        def READ(file):
            file=open(file,READ)
            print("Read access given")

        def WRITE(file):
            file=open(file,WRITE)
            print("write acsess given")
    
    def addResource(self,reso):
        if reso not in self.access:
            self.access.append(reso)

    def addrole(self,ro):
        if ro not in self.roles:
            self.roles.append('role')

    def addUser(self,us):
        if us not in self.user:
            self.user.append('us')


    def addRoleToUser(self,ro,us):
        if us not in self.user:
            self.addUser(us)

        elif ro not in self.roles:
            self.addrole(ro)

        else:
            if us not in self.access_dic:
                self.access_dic[us]=[ro]
            else:
                self.access_dic[us].append(ro)


    def addAccessOnResource(self,acc,reso):
        if acc not in self.access:
            self.access.append(acc)
        elif reso not in self.resource:
            self.resource.append(reso)

        dic={}
        for i in self.access():
            if i not in dic:
                dic[i]=[reso]
            else:
                dic[i].append(reso)

        # {
        # read:image,doc
        # write:image
        # test:pdf
        # }
        

        

        


    
            
        

            
        



            


    
        

        