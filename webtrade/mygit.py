from git import Repo
from os import path,mkdir,walk
#from shutil import copyfile

class gitwrapper:
    def __init__(self,local_folder):
        #self.ssh_key_location=ssh_key
        self.local_folder=local_folder
        if path.isdir(local_folder):
            pass
        else:
            mkdir(local_folder)
    def clone(self,git_url,print_tree=False):
        Repo.clone_from(git_url, self.local_folder)
        if print_tree:
            self.FileTreeMaker(self.local_folder,['.git'])
        
    def pyignore(self):
        _ignore_list=['Thumbs.db','__pycache__/','instance/','.ipynb_checkpoints','.gitignore']
        
        with open(path.join(self.local_folder,'.gitignore'), "w") as file:
            for  line in _ignore_list:
                file.write(line + '\n')
                
    def push_commit(self,git_link,commit_msg='') :        
        repo = Repo(self.local_folder)
        repo.git.add(all=True)
        try:
            repo.git.commit( m=commit_msg )
        except:
            pass
        
        print(repo.git.status() ) 
        self.push_master()
          
    def pull(self):
        repo = Repo(self.local_folder)
        origin=repo.remote(name='origin')
        origin.pull()		
        return origin
        
    def push_master(self):
        origin=self.pull()		
        origin.push()
     
        
    def FileTreeMaker(self,TreeRoot,skip=[]):  

        separator=path.join(' ',' ')[1:-1]

        depthfunc=lambda path:max(len(path.split('/')),len(path.split(separator)))
        rootDepth=depthfunc(TreeRoot)

        skip=list(map(lambda t:path.normpath(t).split(separator), skip))
        skip=[[el,len(el)+rootDepth]for el in skip]

        filesdict={}
        lvlfolderscountdict={}

        prevlevel=-1
        filepreindent=r"┃ "
        bodypostfix="┣━"
        endpostfix="┗━"
        emptyprefix='  '
        
        indents=[filepreindent,emptyprefix,endpostfix]
        for root, dirs, files in walk(TreeRoot):
            skipprint=self.__skipfolders(root,skip,separator,rootDepth)

            if skipprint:
                files=[]
                dirs=[]

            level=depthfunc(root)-depthfunc(TreeRoot)

            if level<=prevlevel:   
                self.__PrintFiles(filesdict,lvlfolderscountdict,bodypostfix,prevlevel,level,filesdict,
                                  PrefixArr,*indents)
            else:postfix=endpostfix

            filesdict[level]=files
            lvlfolderscountdict[level]=[len(dirs),len(files),len(dirs)] 
            PrefixArr=self.__FolderIntend(level,lvlfolderscountdict,bodypostfix,*indents )

            if not skipprint:
                if level>0 :print(''.join(PrefixArr)+'['+path.basename(root)+']')
                else:print(path.basename(root))

            prevlevel=level
        level=0
        self.__PrintFiles(filesdict,lvlfolderscountdict,bodypostfix,prevlevel,level,
                          filesdict,PrefixArr,*indents)         
             

    def __skipfolders(self,_path,_skip,separator,rootDepth):
        res=False
        for skipfolder in _skip:
            if _path.split(separator)[rootDepth:skipfolder[1]]==skipfolder[0]:
                res=True
                break
        return res

    def __PrintFiles(self,arr,lvlfolderscountdict,bodypostfix,prevlevel,level,
                     filesdict,PrefixArr,filepreindent,emptyprefix,endpostfix):
        for i in range(prevlevel,level-1,-1):  
            cut=i-prevlevel-1

            if len(filesdict[i])>0:
                prefix=''
                postfix=''
                if i>0: 
                    prefix=''.join(PrefixArr[:cut])
                    postfix=filepreindent 

                if i>0 and lvlfolderscountdict[i-1][0] <1 and lvlfolderscountdict[i-1][1] ==0 :postfix=emptyprefix
                if lvlfolderscountdict[i][2]==0:postfix+=emptyprefix

                prefix=prefix+postfix

                for  file in filesdict[i][:-1]:
                    print(prefix+bodypostfix+file)
                print(prefix+endpostfix+filesdict[i][-1])     

    def __FolderIntend(self,level,lvlfolderscountdict,bodypostfix,filepreindent,emptyprefix,endpostfix):
        res=[]  
        for i in range(level): 
            if i==level-1:          
                if lvlfolderscountdict[i][1] >0 or lvlfolderscountdict[i][0]>1 :
                    step=bodypostfix
                elif lvlfolderscountdict[i][0] <=1 :step=endpostfix               
            else: 
                if lvlfolderscountdict[i][0] <1 and lvlfolderscountdict[i][1] ==0 :step=emptyprefix
                else:step=filepreindent
            res.append(step)
            if i==level-1:lvlfolderscountdict[i][0]-=1   
        return res