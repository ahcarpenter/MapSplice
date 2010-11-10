#!/usr/bin/python
# Filename: mapsplice_interace.py
# Author: Andrew Hefley Carpenter
# Date: 20 August 2010

import sys
try:
    import gtk
except:
    print >> sys.stderr, "You need to install the python gtk bindings"
    sys.exit(1)
import os
    
class MSInterface:
   
    def on_gettingStarted_destroy(self, widget, data=None):
        gtk.main_quit()

    def on_widget_delete_event(self, widget, event):
        widget.hide()
        return True
    
    def __init__(self):
        self.fileCount = 1
        self.tempCount = 0
        self.readSet = 1
        self.paired = 1
        self.setLabelAdded = 1
        self.row = 0
       
        settings = gtk.settings_get_default()
        settings.props.gtk_button_images = True

        self.builder = gtk.Builder()
        self.builder.add_from_file("config_interface.glade")
        self.actionArea = self.builder.get_object("actionArea")
        self.regionsOfInterest = self.builder.get_object("regionsOfInterest")
        self.regionsToAvoidFileButton = self.builder.get_object("regionsToAvoidFileButton")
        self.gettingStarted = self.builder.get_object("gettingStarted")
        self.treeview = self.builder.get_object("treeview")
        self.readListVP = self.builder.get_object("readListVP")
        self.ioWindow = self.builder.get_object("ioWindow")
        self.bibEntry = self.builder.get_object("bibText")
        self.basicOptionsWindow = self.builder.get_object("basicOptionsWindow")
        self.advancedOptionsWindow = self.builder.get_object("advancedOptionsWindow")
        self.splash = self.builder.get_object("SplashScreen")
        self.fileSelectWindow = self.builder.get_object("FileSelect")
        self.treeView = self.builder.get_object("treeView")
        self.errorMessage = self.builder.get_object("ErrorMessage")
        self.errorLabel = self.builder.get_object("errorLabel")
        self.FileChooserDialog1 = self.builder.get_object("FileChooserDialog1")
        self.FileChooserDialog2 = self.builder.get_object("FileChooserDialog2")
        self.BowtieIndexSelect = self.builder.get_object("BowtieIndexSelect")
        self.BowtieFolderSelect = self.builder.get_object("BowtieFolderSelect")
        self.basenameSetWindow = self.builder.get_object("basenameSetWindow")
        self.basenameLabel = self.builder.get_object("basenameLabel")
        self.MSO = self.builder.get_object("MSO")
        self.MaxH = self.builder.get_object("MaxH")
        self.MSI = self.builder.get_object("MSI")
        self.bowtieBasename = self.builder.get_object("bowtieBasename")
        self.gffFilter = self.builder.get_object("gffFilter")
        self.readFilter = self.builder.get_object("readFilter")
        self.bowtieFilter = self.builder.get_object("bowtieFilter")
        self.envPathInput = self.builder.get_object("envPathInput")
        self.FileChooserDialog3 = self.builder.get_object("FileChooserDialog3")
        self.termOut = self.builder.get_object("termOut")
        self.terminalOutput = self.builder.get_object("terminalOutput")
        self.helpDialog = self.builder.get_object("helpDialog")
        self.aboutdialog1 = self.builder.get_object("aboutdialog1")
        self.chrDirChooser = self.builder.get_object("chrDirChooser")
        self.MOS = self.builder.get_object("MOS")
        self.MH = self.builder.get_object("MH")
        self.MI = self.builder.get_object("MI")
        self.gffFilter.add_pattern("*.gff")
        self.readFilter.add_pattern("*.fa")
        self.readFilter.add_pattern("*.fq")
        self.readFilter.add_pattern("*.fasta")
        self.readFilter.add_pattern("*.fastq")
        self.readFilter.add_pattern("*.txt")
        self.bowtieFilter.add_pattern("*.ebwt")
        self.threads = self.builder.get_object("threads")
        self.anchor_length = self.builder.get_object("anchor_length")
        self.treestore = gtk.ListStore(str, str, str)
        
       
              # create the TreeView using treestore
        self.treeview.set_model(self.treestore)
   
              # create the TreeViewColumn to display the data
        self.id = gtk.TreeViewColumn('Read')
        self.readName = gtk.TreeViewColumn("Filename")
        self.set = gtk.TreeViewColumn("Set")
   
              # add tvcolumn to treeview
        self.treeview.append_column(self.set)
        self.treeview.append_column(self.id)
        self.treeview.append_column(self.readName)
        
              # create a CellRendererText to render the data
        self.cell = gtk.CellRendererText()

              # add the cell to the tvcolumn and allow it to expand
        self.id.pack_start(self.cell, True)
        self.readName.pack_start(self.cell, True)
        self.set.pack_start(self.cell, True)
   
              # set the cell "text" attribute to column 0 - retrieve text
              # from that column in treestore
        self.id.add_attribute(self.cell, 'text', 1)
        self.readName.add_attribute(self.cell, 'text', 2)
        self.set.add_attribute(self.cell, 'text', 0)
   
              # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)
   
        self.readListVP.add(self.treeview)
        
        
        #get input buttons & initialize
        self.segment_mismatches = self.builder.get_object("segment_mismatches")
        self.splice_mismatches = self.builder.get_object("splice_mismatches")
        self.remap_mismatches = self.builder.get_object("remap_mismatches")
        self.min_intron_length = self.builder.get_object("min_intron_length")
        self.max_intron_length = self.builder.get_object("max_intron_length")
        self.read_length = self.builder.get_object("read_len")
        self.segment_length = self.builder.get_object("segment_len")
        self.max_insert = self.builder.get_object("max_insert")
        self.min_output_seg = self.builder.get_object("min_output_seg")
        self.max_hits = self.builder.get_object("max_hits")
        self.canonButton = self.builder.get_object("canonicalRadio")
        self.singleButton = self.builder.get_object("singleButton")
        self.fastaButton = self.builder.get_object("fastaButton")
    

        
        
        #Get Message Dialog's
        self.FileChooserDialog = self.builder.get_object("FileChooserDialog")
        self.ReadSelectHelpBox = self.builder.get_object("readSelectHelp")
        self.RTA = self.builder.get_object("RTA")
        self.OP = self.builder.get_object("OP")
        self.BIB = self.builder.get_object("BIB")
        self.ROI = self.builder.get_object("ROI")
        self.CFD = self.builder.get_object("CFD")
        self.IRF = self.builder.get_object("IRF")
        self.RT = self.builder.get_object("RT")
        self.RL = self.builder.get_object("RL")
        self.SL = self.builder.get_object("SL")
        self.OO = self.builder.get_object("OO")
        self.DTF1 = self.builder.get_object("DTF1")
        self.DTF = self.builder.get_object("DTF")
        self.AL = self.builder.get_object("AL")
        self.ASegM = self.builder.get_object("ASegM")
        self.ASplM = self.builder.get_object("ASplM")
        self.ARM = self.builder.get_object("ARM")
        self.MIL = self.builder.get_object("MIL")
        self.MaxIL = self.builder.get_object("MaxIL")
        self.TH = self.builder.get_object("TH")
        self.SEC = self.builder.get_object("SEC")
        self.MSD = self.builder.get_object("MSD")
        self.RM = self.builder.get_object("RM")
        self.OFJ = self.builder.get_object("OFJ")
        self.GCR = self.builder.get_object("GCR")
        #self.readList = self.builder.get_object("readList")
        #self.readList.append([0,'red',colormap.alloc_color('red')
       # self.readListView = self.builder.get_object("readListView")
        #self.readListView.set_model(self.readList)
        #self.readListView.set_headers_visible(self.readListView.get_headers_visible())
        
        self.builder.connect_signals(self) 

#Getting Started
    def init_input(self):
        self.threads.set_value(1)
        self.threads.set_range(1, 100)
        
        self.anchor_length.set_range(6, 12)
        self.anchor_length.set_value(8)
        
        self.segment_mismatches.set_range(0, 3)
        self.segment_mismatches.set_value(1)
        
        self.splice_mismatches.set_range(0, 10)
        self.splice_mismatches.set_value(1)
        
        self.remap_mismatches.set_range(0, 3)
        self.remap_mismatches.set_value(2)
        
        self.min_intron_length.set_range(1, 100000000)
        self.min_intron_length.set_value(10)
        
        self.max_intron_length.set_range(1, 200000000) #min_intron always <= max_intron
        self.max_intron_length.set_value(200000)
        
        self.read_length.set_value(36)
        self.read_len = 36
        self.read_length.set_range(36, 100000000)
        
        self.segment_length.set_value(18)
        self.segment_length.set_range(18, 25)
        
        self.max_insert.set_range(0, 3)
        self.max_insert.set_value(3)
        
        self.min_output_seg.set_range(1, 2)
        self.min_output_seg.set_value(2)
        
        self.max_hits.set_range(1, 100)
        self.max_hits.set_value(4)
        
        self.canonButton.set_active(True)
        
        self.singleButton.set_active(True)
        self.on_singleButton_clicked(self.singleButton) #so column headers update
        
        self.fastaButton.set_active(True)

    def update_config_file(self):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        reads_file = "reads_file = "
        chromosome_files_directory = "chromosome_files_directory = "
        Bowtieidx = "Bowtieidx = "
        interested_regions = "interested_regions = "
        avoid_regions = "avoid_regions = "
        reads_format = "reads_format = "
        paired_end = "paired_end = "
        read_length = "read_length = "
        segment_length = "segment_length = "
        junction_type = "junction_type = "
        full_running = "full_running = "
        anchor_length = "anchor_length = "
        remove_temp_files = "remove_temp_files = "
        segment_mismatches = "segment_mismatches = "
        splice_mismatches = "splice_mismatches = "
        remap_mismatches = "remap_mismatches = "
        min_intron_length = "min_intron_length = "
        max_intron_length = "max_intron_length = "
        threads = "threads = "
        max_hit = "max_hit = "
        max_insert = "max_insert = "
        min_output_seg = "min_output_seg = "
        search_whole_chromosome = "search_whole_chromosome = "
        map_segment_directly = "map_segment_directly = "
        run_MapPER = "run_MapPER = "
        do_fusion = "do_fusion = "
        do_cluster = "do_cluster = "
        
        for item in configFileList:
            if chromosome_files_directory in item:
                item = chromosome_files_directory + self.chrDirChooser.get_filename() + "\n"
            
            if Bowtieidx in item:
                dir = os.path.abspath(os.curdir)
                dir = os.path.split(dir)[0].rstrip() + "/BowtieIndexFiles"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                item = Bowtieidx + dir + "/index\n"

            if interested_regions in item and self.regionsOfInterest.get_filename() != None:
                item = interested_regions + self.regionsOfInterest.get_filename() +"\n"
                
            if avoid_regions in item and self.regionsToAvoidFileButton.get_filename() != None:
                item = avoid_regions + self.regionsToAvoidFileButton.get_filename() +"\n"

            if reads_format in item:
                button = self.builder.get_object("fastaButton")
                if button.get_active:
                    item = reads_format + "FASTA\n"
                else:
                    item = reads_format + "FASTQ\n"
                    
            if paired_end in item:
                item = paired_end + "FASTQ\n"

            if read_length in item:
                item = read_length + "FASTQ\n"

            if segment_length in item:
                item = segment_length + "FASTQ\n"

            if junction_type in item:
                item = junction_type + "FASTQ\n"

            if full_running in item:
                item = full_running + "FASTQ\n"

            if anchor_length in item:
                item = anchor_length + "FASTQ\n"

            if remove_temp_files in item:
                item = remove_temp_files + "FASTQ\n"

            if segment_mismatches in item:
                item = segment_mismatches + "FASTQ\n"

            if splice_mismatches in item:
                item = splice_mismatches + "FASTQ\n"

            if remap_mismatches in item:
                item = remap_mismatches + "FASTQ\n"

            if min_intron_length in item:
                item = min_intron_length + "FASTQ\n"

            if max_intron_length in item:
                item = max_intron_length + "FASTQ\n"

            if threads in item:
                item = threads + "FASTQ\n"

            if max_hit in item:
                item = max_hit + "FASTQ\n"

            if max_insert in item:
                item = max_insert + "FASTQ\n"

            if min_output_seg in item:
                item = min_output_seg + "FASTQ\n"

            if search_whole_chromosome in item:
                item = search_whole_chromosome + "FASTQ\n"

            if map_segment_directly in item:
                item = map_segment_directly + "FASTQ\n"

            if run_MapPER in item:
                item = run_MapPER + "FASTQ\n"

            if do_fusion in item:
                item = do_fusion + "FASTQ\n"

            if do_cluster in item:
                item = do_cluster + "FASTQ\n"
            
            self.configFileWrite.write(item)
        
       
        self.configFileWrite.close()

    def on_main_delete_event(self, widget, event):
        exit()

    def on_help_clicked(self, widget):
        self.helpDialog.show()
        
    def on_aa_button_clicked(self, widget):
        print "HELLO"
        
    def on_main_help_clicked(self, widget):
        self.aboutdialog1.show()
        
    def on_executeMS_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileRead = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        var = "first_run = "
        var2 = "envPath = "
        
        for item in configFileList:
            if var in item and "y" in item:
                self.configFileRead.close()
                self.envPathInput.show()
            elif var in item and "first_run = n" in item:
                for item2 in configFileList:
                    if var2 in item2:
                        item3 = item2[10:].rstrip() + "mapsplice_segments.py"
                        #print item3
                        if os.path.exists(item3) == 1:
                            #envPath = "$PATH:" + item2[10:].rstrip() + "/"
                            #os.putenv("PATH",envPath)
                            self.configFileRead.close()
                            configFilePath = item2[10:].rstrip()
                            configFilePath = os.path.split(configFilePath)[0]
                            configFilePath = os.path.split(configFilePath)[0]
                            os.system("python " + item3 + " " + "../MapSplice.cfg")
                        else:
                            self.configFileRead.close()
                            self.envPathInput.show()

    def on_envPathSet_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w") #change to ../../MapSplice.cfg
        var = "envPath"
        var2 = "first_run"
        
        for item in configFileList:
            if var in item:
                #os.getenv("PATH")
                item = "envPath = " + self.FileChooserDialog3.get_filename() + "/" + "\n"
                self.item = item
            if var2 in item:
                item = "first_run = n \n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        self.envPathInput.hide()
        mapsplicePath = self.FileChooserDialog3.get_filename() + "/mapsplice_segments.py"
        if os.path.exists(mapsplicePath):
            #os.getenv("PATH")
            #os.putenv("PATH",os.getenv("PATH") + ":" +self.FileChooserDialog3.get_filename() + "/")
            self.gettingStarted.show()
            configFilePath = self.FileChooserDialog3.get_filename()
            os.system("python " + self.FileChooserDialog3.get_filename() + "/mapsplice_segments.py " + os.path.split(configFilePath)[0] + "/../MapSplice.cfg")
        else:
            self.envPathInput.show()
        
    def on_ioButton_clicked(self, widget):
        self.ioWindow.show()
        
    def on_aboutdialog_close_clicked(self, widget, response_id):
        widget.hide()
        return True
        
    def on_cancel_clicked(self, widget):
        parent = widget.get_parent()
        grandparent = parent.get_parent()
        greatgrandparent = grandparent.get_parent()
        greatgreatgrandparent = greatgrandparent.get_parent()
        greatgreatgrandparent.hide()
        
    def on_cancelIO_clicked(self, widget):
        parent = widget.get_parent()
        grandparent = parent.get_parent()
        greatgrandparent = grandparent.get_parent()
        greatgreatgrandparent = greatgrandparent.get_parent()
        greatgreatgreatgrandparent = greatgreatgrandparent.get_parent()
        greatgreatgreatgrandparent.hide()
        
    def on_basicOptionsButton_clicked(self, widget):
        self.basicOptionsWindow.show()
        
    def on_advancedOptionsButton_clicked(self, widget):
        self.advancedOptionsWindow.show()
        
    def on_doneButton_clicked(self, widget):
        parent = widget.get_parent()
        grandparent = parent.get_parent()
        greatgrandparent = grandparent.get_parent()
        greatgreatgrandparent = greatgrandparent.get_parent()
        greatgreatgrandparent.hide()
        
        
# I/O Window
    def gtk_MainWindow_show(self, widget):
        parent = widget.get_parent()
        grandparent = parent.get_parent()
        greatGrandParent = grandparent.get_parent()
        greatGrandParent.hide()
        
    def gtk_basenameInput_hide(self, widget):
        parent = widget.get_parent()
        grandparent = parent.get_parent()
        greatGrandParent = grandparent.get_parent()
        greatgreatGrandParent = greatGrandParent.get_parent()
        greatgreatGrandParent.hide()
        
    def on_selectFileButton_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w") #change to .. / ../MapSplice.cfg
        if self.fileCount == 1 and self.paired == 1:
            self.file = self.FileChooserDialog.get_filename()
            self.fileCountStr = str(self.fileCount)
            self.readSetStr = str(self.readSet)            
            self.iter = self.treestore.insert(self.row, (self.readSetStr, self.fileCountStr, os.path.basename(self.FileChooserDialog.get_filename())))
            self.iterPath = self.treestore.get_path(self.iter)
            self.row = self.row + 1
            self.fileCount = self.fileCount + 1
        elif self.paired == 1:
            if self.fileCount == 3:
                self.fileCount = 1
            if self.fileCount == 1:
                self.readSet = self.readSet + 1
            self.fileCountStr = str(self.fileCount)
            self.readSetStr = str(self.readSet)
            self.fileCount = self.fileCount + 1
            self.file = self.file + "," + self.FileChooserDialog.get_filename()
            self.iter = self.treestore.insert(self.row, (self.readSetStr, self.fileCountStr, os.path.basename(self.FileChooserDialog.get_filename())))
            self.iterPath = self.treestore.get_path(self.iter)
            self.row = self.row + 1
         #for single end
        if self.fileCount == 1 and self.paired == 0:
            self.file = self.FileChooserDialog.get_filename()
            self.fileCountStr = str(self.fileCount)
            self.readSetStr = str(self.readSet)
            self.iter = self.treestore.insert(self.row, (None, self.fileCountStr, os.path.basename(self.FileChooserDialog.get_filename())))
            self.iterPath = self.treestore.get_path(self.iter)
            self.row = self.row + 1
            self.fileCount = self.fileCount + 1
        elif self.paired == 0:
            self.fileCountStr = str(self.fileCount)
            self.fileCount = self.fileCount + 1
            self.file = self.file + "," + self.FileChooserDialog.get_filename()
            self.iter = self.treestore.insert(self.row, (None, self.fileCountStr, os.path.basename(self.FileChooserDialog.get_filename())))
            self.iterPath = self.treestore.get_path(self.iter)
            self.row = self.row + 1
            
        var = "reads_file ="
        
        for item in configFileList:
            if var in item:
                item = "reads_file = " + self.file + "\n"
            self.configFileWrite.write(item)
         
        self.configFileWrite.close() 
        self.fileSelectWindow.hide()
        
    def on_removeRead_clicked(self, widget):
        
        self.iterParent = self.treestore.iter_parent(self.treestore.get_iter(self.iterPath))
        self.treestore.remove(self.iter)
        self.treestore.swap(self.iterParent, self.iter)
        
    def on_read_clicked(treeview, path, view_column, user_param1):
        #self.currentTreeView = treeview
        #self.path = path
        #self.view_column = view_column
        print path
           
    def gtk_FileSelect_show(self, widget):
        self.fileSelectWindow.show()
        
    def on_resetReadLabel_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w") #change to .. / ../MapSplice.cfg
        var = "reads_file = "
        for item in configFileList:
            if var in item:
                item = "reads_file = \n"
            self.configFileWrite.write(item)
        self.configFileWrite.close()
        self.row = 0
        if self.setLabelAdded != 1 and self.paired != 0:
            self.treeview.append_column(self.set)
        self.fileCount = 1
        self.treestore.clear()
        
    def on_regionsToAvoidFileButton_file_set(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w") #change to ../../MapSplice.cfg
        var = "#avoid_regions ="
        
        for item in configFileList:
            if var in item:
                item = "#avoid_regions = " + widget.get_filename() + "\n"
            self.configFileWrite.write(item)
        self.configFileWrite.close()
        
    def on_outputPathFileButton_file_set(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w") #change to ../../MapSplice.cfg
        var = "output_dir ="
        
        for item in configFileList:
            if var in item:
                item = "output_dir = " + widget.get_filename() + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_bibButton_clicked(self, widget):
        self.BowtieIndexSelect.show()
        
    def on_index_select_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r") #change to ../../MapSplice.cfg
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w") #change to ../../MapSplice.cfg
        var = "Bowtieidx"
        
        for item in configFileList:
            if var in item:
                fileName = self.FileChooserDialog1.get_filename()
                suffix = ".1.ebwt"
                fileName = fileName[:-len(suffix)]
                self.bowtieBasename.set_markup("<i>" + os.path.basename(fileName) + "</i>")
                item = "Bowtieidx = " + fileName + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        self.BowtieIndexSelect.hide()
        
    def on_bowtieFolderSelect_clicked(self, widget):
        self.BowtieFolderSelect.show()
        

    def on_bowtieFolderButton_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        dir = os.path.abspath(os.curdir)
        dir = os.path.split(dir)[0].rstrip() + "/BowtieIndexFiles"
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "Bowtieidx"
        
        for item in configFileList:
            if var in item:
                item = "Bowtieidx = " + dir
                self.item = item
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        self.basenameSetWindow.show()
        
    def on_basenameSetButton_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "Bowtieidx"
        
        for item in configFileList:
            if var in item:
                item = self.item + "/" + self.basenameLabel.get_text() + "\n\n"
            self.configFileWrite.write(item)
       
        self.bowtieBasename.set_markup("<i>" + self.basenameLabel.get_text() + "</i>")       
        self.configFileWrite.close()
        self.basenameSetWindow.hide()
         
    def on_ROA_file_set(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "#interested_regions ="
        
        for item in configFileList:
            if var in item:
                item = "interested = " + widget.get_filename() + "\n"
            self.configFileWrite.write(item)
        self.configFileWrite.close()
        
    def on_CFD_selection_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "chromosome_files_dir ="
        
        for item in configFileList:
            if var in item:
                item = "chromosome_files_dir = " + widget.get_filename() + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
#Basic Options
    def on_fastaButton_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "reads_format ="
        
        for item in configFileList:
            if var in item:
                item = "reads_format = " + "FASTA\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_fastqButton_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "reads_format ="
        
        for item in configFileList:
            if var in item:
                item = "reads_format = " + "FASTQ\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_singleButton_clicked(self, widget):
        
        if self.setLabelAdded != 0:
            self.treestore.clear()
            self.row = 0
        self.setLabelAdded = 0;
        self.treeview.remove_column(self.set)
        #self.treeview.remove_column(self.treeview.get_column(3))
        self.fileCount = 1
        self.paired = 0
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "paired_end ="
        
        for item in configFileList:
            if var in item:
                item = "paired_end = " + "no\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_pairedendButton_clicked(self, widget):
        if self.setLabelAdded != 1:
            self.treestore.clear()
            self.row = 0
            self.treeview.insert_column(self.set, 0)
        self.setLabelAdded = 1;
        self.fileCount = 1
        self.paired = 1
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "paired_end ="
        
        for item in configFileList:
            if var in item:
                item = "paired_end = " + "yes\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_RL_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "read_length ="
        read_len = str(self.read_length.get_value_as_int())
        
        for item in configFileList:
            if var in item:
                item = "read_length = " + read_len + "\n"
            self.configFileWrite.write(item)
        self.configFileWrite.close()    
            
        self.read_len = int(read_len)
        seg_length = self.read_len / 2
        self.segment_length.set_value(seg_length)
        min_output_seg_max = self.read_len / seg_length
        self.min_output_seg.set_range(1, min_output_seg_max)

    def on_SL_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "segment_length ="
        
        for item in configFileList:
            if var in item:
                item = "segment_length = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
        self.configFileWrite.close()
        
        min_output_seg_max = self.read_len / widget.get_value_as_int()
        self.min_output_seg.set_range(1, min_output_seg_max)
        
    def key_press_event(self, widget, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        if "Return" in keyname or "Esc" in keyname:
            widget.hide();
            
    def key_press_event_basename(self, widget, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        if "Return" in keyname:
            self.on_basenameSetButton_clicked(widget)
        if "Esc" in keyname:
            widget.hide();
            
    def key_press_event_main(self, widget, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        if "Esc" in keyname:
            exit();
 
#Advanced Options
    def on_canon_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "junction_type ="
        
        for item in configFileList:
            if var in item:
                item = "junction_type = " + "canonical\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_noncanon_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "junction_type ="
        
        for item in configFileList:
            if var in item:
                item = "junction_type = " + "non-canonical\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_semicanon_clicked(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "junction_type ="
        
        for item in configFileList:
            if var in item:
                item = "junction_type = " + "semi-canonical\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_remap_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "full_running = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "full_running = " + "yes\n"
                else:
                    item = "full_running = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
        
    def on_deletetemp_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "remove_temp_files = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "remove_temp_files = " + "yes\n"
                else:
                    item = "remove_temp_files = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
        
    def on_sec_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "search_whole_chromosome = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "search_whole_chromosome = " + "yes\n"
                else:
                    item = "search_whole_chromosome = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
        
    def on_msd_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "map_segment_directly = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "map_segment_directly = " + "yes\n"
                else:
                    item = "map_segment_directly = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
        
    def on_mapper_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "run_MapPER = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "run_MapPER = " + "yes\n"
                else:
                    item = "run_MapPER = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
        
    def on_ofj_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "do_fusion = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "do_fusion = " + "yes\n"
                else:
                    item = "do_fusion = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
        
    def on_gcr_toggled(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "#do_cluster = "
        for item in configFileList:
            if var in item:
                if widget.get_active():
                    item = "#do_cluster = " + "yes\n"
                else:
                    item = "#do_cluster = " + "no\n"
            self.configFileWrite.write(item)
           
        self.configFileWrite.close()
    
    def on_anchor_length_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "anchor_length ="
        
        for item in configFileList:
            if var in item:
                item = "anchor_length = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
    
    def on_segment_mismatches_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "segment_mismatches ="
        
        for item in configFileList:
            if var in item:
                item = "segment_mismatches = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
    
    def on_splice_mismatches_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "splice_mismatches ="
        
        for item in configFileList:
            if var in item:
                item = "splice_mismatches = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_remap_mismatches_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "remap_mismatches ="
        
        for item in configFileList:
            if var in item:
                item = "remap_mismatches = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_max_hits_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "max_hits ="
        
        for item in configFileList:
            if var in item:
                item = "max_hits = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_min_output_seg_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "min_output_seg ="
        
        for item in configFileList:
            if var in item:
                item = "min_output_seg = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_max_insert_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "max_insert ="
        
        for item in configFileList:
            if var in item:
                item = "max_insert = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_min_intron_length_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "min_intron_length ="
        
        for item in configFileList:
            if var in item:
                item = "min_intron_length = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        
    def on_max_intron_length_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "max_intron_length ="
        
        for item in configFileList:
            if var in item:
                item = "max_intron_length = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
        #self.min_intron_length.set_value(widget.get_value_as_int())
        self.min_intron_length.set_range(1, widget.get_value_as_int())
        
    def on_threads_value_changed(self, widget):
        configFile = open("../MapSplice.cfg", "r")
        configFileList = configFile.readlines()
        configFile.close()
        self.configFileWrite = open("../MapSplice.cfg", "w")
        var = "threads ="
        
        for item in configFileList:
            if var in item:
                item = "threads = " + str(widget.get_value_as_int()) + "\n"
            self.configFileWrite.write(item)
       
        self.configFileWrite.close()
       
# Help Boxes   
    def on_helpCloseButton_clicked(self, widget):
        parent = widget.get_parent()
        grandparent = parent.get_parent()
        greatGrandParent = grandparent.get_parent()
        greatGrandParent.hide()
  
    def on_showReadSelectHelp_clicked(self, widget):
        self.ReadSelectHelpBox.show()
        
    def on_max_smallindel_help_clicked(self, widget):
        self.MSI.show()
        
    def on_max_hits_help_clicked(self, widget):
        self.MaxH.show()
        
    def on_max_smallindel_help_clicked(self, widget):
        self.MSI.show()
    
    def on_closeReadSelectHelp_clicked(self, widget):
        self.ReadSelectHelpBox.hide()
        
    def on_showRegionsToAvoidHelp_clicked(self, widget):
        self.RTA.show()
    
    def on_closeRegionsToAvoidHelp_clicked(self, widget):
        self.RTA.hide()
        
    def on_showOutputPathHelp_clicked(self, widget):
        self.OP.show()
    
    def on_closeOutputPathHelp_clicked(self, widget):
        self.OP.hide()
        
    def on_showBowtieIndexBasenameHelp_clicked(self, widget):
        self.BIB.show()
        
    def on_min_output_seg_help_clicked(self, widget):
        self.MSO.show()
        
    def on_max_hit_help_clicked(self, widget):
        self.MH.show()
        
    def on_max_insert_help_clicked(self, widget):
        self.MI.show()
    
    def on_closeBowtieIndexBasenameHelp_clicked(self, widget):
        self.BIB.hide()
        
    def on_showRegionsOfInterestHelp_clicked(self, widget):
        self.ROI.show()
    
    def on_closeRegionsOfInterestHelp_clicked(self, widget):
        self.ROI.hide()
        
    def on_showChromosomeFilesDirectoryHelp_clicked(self, widget):
        self.CFD.show()
    
    def on_closeChromosomeFilesDirectoryHelp_clicked(self, widget):
        self.CFD.hide()
        
    def on_showInputReadFormatHelp_clicked(self, widget):
        self.IRF.show()
    
    def on_closeInputReadFormatHelp_clicked(self, widget):
        self.IRF.hide()
        
    def on_showReadTypeHelp_clicked(self, widget):
        self.RT.show()
    
    def on_closeReadTypeHelp_clicked(self, widget):
        self.RT.hide()
        
    def on_showReadLengthHelp_clicked(self, widget):
        self.RL.show()
    
    def on_closeReadLengthHelp_clicked(self, widget):
        self.RL.hide()
        
    def on_showSegmentLengthHelp_clicked(self, widget):
        self.SL.show()
    
    def on_closeSegmentLengthHelp_clicked(self, widget):
        self.SL.hide()
        
    def on_showOutputOrderingHelp_clicked(self, widget):
        self.OO.show()
    
    def on_closeOutputOrderingHelp_clicked(self, widget):
        self.OO.hide()
        
    def on_showRemapHelp_clicked(self, widget):
        self.DTF1.show()
    
    def on_closeRemapHelp_clicked(self, widget):
        self.R.hide()
        
    def on_showDeleteTempFilesHelp_clicked(self, widget):
        self.DTF.show()
    
    def on_closeDeleteTempFilesHelp_clicked(self, widget):
        self.DTF.hide()
        
    def on_showAnchorLengthHelp_clicked(self, widget):
        self.AL.show()
    
    def on_closeAnchorLengthHelp_clicked(self, widget):
        self.AL.hide()
        
    def on_showAllowedSegmentMismatchesHelp_clicked(self, widget):
        self.ASegM.show()
    
    def on_closeAllowedSegmentMismatchesHelp_clicked(self, widget):
        self.ASegM.hide()
        
    def on_showAllowedSpliceMismatchesHelp_clicked(self, widget):
        self.ASplM.show()
    
    def on_closeAllowedSpliceMismatchesHelp_clicked(self, widget):
        self.ASplM.hide()
        
    def on_showAllowedRemapMismatchesHelp_clicked(self, widget):
        self.ARM.show()
    
    def on_closeAllowedRemapMismatchesHelp_clicked(self, widget):
        self.ARM.hide()
        
    def on_showMinIntronLengthHelp_clicked(self, widget):
        self.MIL.show()
    
    def on_closeMinIntronLengthHelp_clicked(self, widget):
        self.MIL.hide()
        
    def on_showMaxIntronLengthHelp_clicked(self, widget):
        self.MaxIL.show()
    
    def on_closeMaxIntronLengthHelp_clicked(self, widget):
        self.MaxIL.hide()
        
    def on_showThreadsHelp_clicked(self, widget):
        self.TH.show()
    
    def on_closeThreadsHelp_clicked(self, widget):
        self.TH.hide()
        
    def on_showSearchEntireChromHelp_clicked(self, widget):
        self.SEC.show()
    
    def on_closeSearchEntireChromHelp_clicked(self, widget):
        self.SEC.hide()
    
    def on_showMapSegDirectlyHelp_clicked(self, widget):
        self.MSD.show()
    
    def on_closeMapSegDirectlyHelp_clicked(self, widget):
        self.MSD.hide()
        
    def on_showRunMapPERHelp_clicked(self, widget):
        self.RM.show()
    
    def on_closeRunMapPERHelp_clicked(self, widget):
        self.RM.hide()
        
    def on_showOutputFusionJunctionHelp_clicked(self, widget):
        self.OFJ.show()
    
    def on_closeOutputFusionJunctionHelp_clicked(self, widget):
        self.OFJ.hide()
 
    def on_showGenerateClusterRegionstHelp_clicked(self, widget):
        self.GCR.show()
    
    def on_closeGenerateClusterRegionsHelp_clicked(self, widget):
        self.GCR.hide()
          
if __name__ == "__main__":
    configInterface = MSInterface()
    configInterface.gettingStarted.show()
    configInterface.init_input()
    configInterface.update_config_file()
    gtk.main()
