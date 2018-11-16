#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:05:59 2018

@author: zel0rd
"""

import struct
with open('C:/Users/Soo/Desktop/정리/문서/실습예제/실습예제/02_PE_File_Format/13_PE_File_Format/bin/notepad.exe', "rb") as f:

    print("--------------------IMAGE_DOS_HEADER--------------------")
    #IMAGE_DOS_HEADER == IDH
    IDH_Signature = f.read(2)
    IDH_Signature_h = IDH_Signature.hex()
    print(IDH_Signature_h.upper() + "\t\t\tSignature")

    f.seek(0x02)
    IDH_Bytes = f.read(2)
    IDH_Bytes_h = IDH_Bytes.hex()
    print(IDH_Bytes_h.upper() + "\t\t\tBytes on Last Page of File")

    f.seek(0x04)
    IDH_Pages = f.read(2)
    IDH_Pages_h = IDH_Pages.hex()
    print(IDH_Pages_h.upper() + "\t\t\tPages in File")

    f.seek(0x06)
    IDH_Relocations = f.read(2)
    IDH_Relocations_h = IDH_Relocations.hex()
    print(IDH_Relocations_h.upper() + "\t\t\tRelocations")

    f.seek(0x08)
    IDH_Size = f.read(2)
    IDH_Size_h = IDH_Size.hex()
    print(IDH_Size_h.upper() + "\t\t\tSize of Header in Paragraphs")

    f.seek(0x0A)
    IDH_Minimum = f.read(2)
    IDH_Minimum_h = IDH_Minimum.hex()
    print(IDH_Minimum_h.upper() + "\t\t\tMinimum Extra Paragraphs")

    f.seek(0x0c)
    IDH_Maximum = f.read(2)
    IDH_Maximum_h = IDH_Minimum.hex()
    print(IDH_Maximum_h.upper() + "\t\t\tMaximum Extra Paragraphs")

    f.seek(0x0e)
    IDH_InitialSS = f.read(2)
    IDH_InitialSS_h = IDH_InitialSS.hex()
    print(IDH_InitialSS_h.upper() + "\t\t\tInitial (relative) SS")

    f.seek(0x10)
    IDH_InitialSP = f.read(2)
    IDH_InitialSP_h = IDH_InitialSP.hex()
    print(IDH_InitialSP_h.upper() + "\t\t\tInitial SP")

    f.seek(0x12)
    IDH_Checksum = f.read(2)
    IDH_Checksum_h = IDH_Checksum.hex()
    print(IDH_Checksum_h.upper() + "\t\t\tChecksum")

    f.seek(0x14)
    IDH_InitialIP = f.read(2)
    IDH_InitialIP_h = IDH_InitialIP.hex()
    print(IDH_InitialIP_h.upper() + "\t\t\tInitial IP")

    f.seek(0x16)
    IDH_InitialCS = f.read(2)
    IDH_InitialCS_h = IDH_InitialCS.hex()
    print(IDH_InitialCS_h.upper() + "\t\t\tInitial (relative) CS")

    f.seek(0x18)
    IDH_Offset = f.read(2)
    IDH_Offset_h = IDH_Offset.hex()
    print(IDH_Offset_h.upper() + "\t\t\tOffset to Relocation Table")

    f.seek(0x1a)
    IDH_Overlay = f.read(2)
    IDH_Overlay_h = IDH_Overlay.hex()
    print(IDH_Overlay_h.upper() + "\t\t\tOverlay Number")

    f.seek(0x1c)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x1e)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x20)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x22)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x24)
    IDH_OEMId = f.read(2)
    IDH_OEMId_h = IDH_OEMId.hex()
    print(IDH_OEMId_h.upper() + "\t\t\tOEM Identifier")

    f.seek(0x26)
    IDH_OEMIn = f.read(2)
    IDH_OEMIn_h = IDH_OEMIn.hex()
    print(IDH_OEMIn_h.upper() + "\t\t\tOEM Information")

    f.seek(0x28)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x2A)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x2C)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x2E)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x30)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x32)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x34)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x36)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x38)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x3A)
    IDH_Reserved = f.read(2)
    IDH_Reserved_h = IDH_Reserved.hex()
    print(IDH_Reserved_h.upper() + "\t\t\tReserved")

    f.seek(0x3C)
    IDH_lfanew = f.read(4)
    IDH_lfanew_h = IDH_lfanew.hex()
    print(IDH_lfanew_h.upper() + "\t\tOffset to New EXE Header")

#    print("--------------------------------------------------------\n")
    print("--------------------IMAGE_NT_HEADERS--------------------")
    #IMAGE_NT_HEADERS == INH
    f.seek(0xe0)
    INT_Siganature = f.read(4)
    INT_Siganature_h = INT_Siganature.hex()
    print(INT_Siganature_h.upper() + "\t\tSignature")

    print("--------------------IMAGE_FILE_HEADER--------------------")
    #IMAGE_FILE_HEADER == IFH
    f.seek(0xe4)
    IFH_Machine = f.read(2)
    IFH_Machine_h = IFH_Machine.hex()
    print(IFH_Machine_h.upper() + "\t\t\tMachine")

    f.seek(0xe6)
    IFH_NumberSec = f.read(2)
    IFH_NumberSec_h = IFH_NumberSec.hex()
    print(IFH_NumberSec_h.upper() + "\t\t\tNumber of Sections")

    f.seek(0xe8)
    IFH_Time = f.read(4)
    IFH_Time_h = IFH_Time.hex()
    print(IFH_Time_h.upper() + "\t\tTime Date Stamp")

    f.seek(0xec)
    IFH_Pointer = f.read(4)
    IFH_Pointer_h = IFH_Pointer.hex()
    print(IFH_Pointer_h.upper() + "\t\tPointer to Symbol Table")

    f.seek(0xf0)
    IFH_NumberSym = f.read(4)
    IFH_NumberSym_h = IFH_NumberSym.hex()
    print(IFH_NumberSym_h.upper() + "\t\tNumber of Symbols")

    f.seek(0xf4)
    IFH_Size = f.read(2)
    IFH_Size_h = IFH_Size.hex()
    print(IFH_Size_h.upper() + "\t\t\tSize of OPtional Header")

    f.seek(0xf6)
    IFH_Characteristics = f.read(2)
    IFH_Characteristics_h = IFH_Characteristics.hex()
    print(IFH_Characteristics_h.upper() + "\t\t\tCharacteristics")

    print("--------------------IMAGE_OPTIONAL_HEADER--------------------")