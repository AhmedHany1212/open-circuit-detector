class class_of_edits:
    def __init__(self,line,nodes,words,n):
        self.line = line
        self.nodes = nodes
        self.words = words
        self.n = n
      
    #make multilines as one line splited to words list
    def merge_lines(self,words,line):
        self.words=self.words+self.line.split()
        self.words.remove("+")
        return self.words

    #add nodes to nodes list by copying words list to it and remove ".subckt" and subckt name
    def add_subckt_nodes(self, nodes, words):
        self.nodes = self.words.copy()
        self.nodes.pop(0)
        self.nodes.pop(0)
        return self.nodes
     
    #add subckt instantiation nodes in nodes list 
    def add_subckt_inst_nodes(self,nodes, words):
        self.nodes.extend(self.words)
        self.nodes.pop(len(nodes)-1)
        return self.nodes

    #add node (second and third word in line) to nodes list 
    def add_element_nodes(self,nodes,words):
        self.nodes.append(self.words[1])
        self.nodes.append(self.words[2])
        return self.nodes

    #find non-repeating elements in an list    
    def find_non_repeating(self,nodes, n):
        mp = dict()
        # Traverse through list elements
        # and count frequencies
        for i in range(self.n):
            if self.nodes[i] in mp.keys():
                mp[self.nodes[i]] += 1
            else:
                mp[self.nodes[i]] = 1
        # Traverse through map and print
        # frequencies
        for x in mp:
            if mp[x]==1 :
                print("node "+x+" is open");