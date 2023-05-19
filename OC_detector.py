import edit_lists

with open('netlist.sp','r') as file:
    num_subckt=0
    nodes=[]
    words=[]
    subckt_names=[]
    line=""
    # reading each line  
    for count, line in enumerate(file):
        
        #Skip the empty line and the commented line
        if len(line)==1 or line[0]=='*' :
            continue
        
        # make multilines that start with '+' as one line splited to words list
        if line[0]=='+':
            words=edit_lists.class_of_edits(line,nodes,words,len(nodes)).merge_lines(words,line)
        else:
            #split line into words list
            words=line.split()
            
        #add subckt name to subckt_names list if word ".subckt" found
        if(line.find(".subckt")!= -1):
            subckt_names.append(words[1])
            
        #add nodes to nodes list by copying words list to it and remove ".subckt" and subckt name
        if(words[0]==".subckt"):
            nodes=edit_lists.class_of_edits(line,nodes,words,len(nodes)).add_subckt_nodes(nodes,words)

        #add subckt instantiation nodes in nodes list 
        if(words[len(words)-1] in subckt_names):
            words.pop(0)
            nodes=edit_lists.class_of_edits(line,nodes,words,len(nodes)).add_subckt_inst_nodes(nodes, words)
        
        #add capicitors node (second and third word in line) to nodes list 
        if(line[0]=='c' and line[len(line)-2]=='f' and len(words)==4):
            nodes=edit_lists.class_of_edits(line,nodes,words,len(nodes)).add_element_nodes(nodes,words)
        
        #add resistors node (second and third word in line) to nodes list 
        if(line[0]=='r' and words[3].find('.') != -1 and len(words)==4):
            nodes=edit_lists.class_of_edits(line,nodes,words,len(nodes)).add_element_nodes(nodes,words)
      
        #add X0 node (second and third word in line) to nodes list 
        if(line[0]=='X' and line.find("W=")!= -1 and line.find("L=")!= -1):
            nodes=edit_lists.class_of_edits(line,nodes,words,len(nodes)).add_element_nodes(nodes,words)
        
        #remove nodes from nodes list after .edns line
        if(words[0]==".ends"):
            #get the open circuit node (that reapeted one time)
            edit_lists.class_of_edits(line,nodes,words,len(nodes)).find_non_repeating(nodes,len(nodes))
            nodes.clear()
            num_subckt+=1

file.close()
