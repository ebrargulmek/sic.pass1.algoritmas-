opcode_table = {
    "ADD": "18", "ADDF": "58", "ADDR": "90", "AND": "40", "CLEAR": "B4",
    "COMP": "28", "COMPF": "88", "COMPR": "A0", "DIV": "24", "DIVF": "64",
    "DIVR": "9C", "FIX": "C4", "FLOAT": "C0", "HIO": "F4", "J": "3C", "JEQ": "30",
    "JGT": "34", "JLT": "38", "JSUB": "48", "LDA": "00", "LDB": "68", "LDCH": "50", "LDF": "70",
    "LDL": "08", "LDS": "6C", "LDT": "74", "LDX": "04", "LPS": "D0", "MUL": "20", "MULF": "60", "MULR": "98",
    "STL": "14", "STS": "7C", "STSW": "E8", "STT": "84", "STX": "10", "SUB": "1C", "SUBF": "5C",
    "SUBR": "94", "SVC": "B0", "TD": "E0", "TIO": "F8", "TIX": "2C", "TIXR": "B8", "WD": "DC",
    "NORM": "C8", "OR": "44", "RD": "D8", "RMO": "AC", "RSUB": "4C", "SHIFTL": "A4", "SHIFTR": "A8",
    "SIO": "F0", "SSK": "EC", "STA": "0C", "STB": "78", "STCH": "54", "STF": "80", "STI": "D4", "TLX":" "
}
def parse_line(line):
    #Her bir kaynak kod satırını ayrıştırarak etiket, işlem kodu ve operandı ayıklar.
    parts = line.split()
    label, opcode, operand = None, None, None
    if len(parts) == 3:
        label, opcode, operand = parts
    elif len(parts) == 2:
        opcode, operand = parts
    return label, opcode, operand

def pass1(source_lines):
    # Assembler'ın ilk geçişini gerçekleştirir ve sembol tablosunu döndürür.
    LOCCTR = 0
    SYMTAB = {}
    start_address = None

    
    for line in source_lines:
        if line.strip().startswith('.'):  # Yorum satırlarını atlar
            continue

        label, opcode, operand = parse_line(line)

        if opcode == 'START':  # Başlangıç adresini belirler
            start_address = int(operand, 16)
            LOCCTR = start_address
            continue

        if label:  # Sembol tablosuna etiketi ve mevcut LOCCTR'yi ekler
            if label in SYMTAB:
                raise ValueError(f"Error: Duplicate symbol `{label}`.")
            SYMTAB[label] = LOCCTR
        
        # LOCCTR'yi artırır, komutun boyutuna göre
        if opcode == 'RESW':
            LOCCTR += int(operand) * 3
        elif opcode == 'RESB':
            LOCCTR += int(operand)
        elif opcode == 'WORD':
            LOCCTR += 3
        elif opcode == 'BYTE':
            if operand.startswith("C'"):
                LOCCTR += len(operand) - 3  #C' ve son tırnak için -3
            elif operand.startswith("X'"):
                LOCCTR += (len(operand) - 3) // 2  #X' ve son tırnak için -3 ve //2
        else:
            LOCCTR += 3  #Diğer tüm durumlar için varsayılan olarak 3 byte artır

        if opcode == 'END':  #'END' komutunda durur
            break


    return SYMTAB, start_address, LOCCTR

def read_source_file(file_name):
    with open(file_name, 'r') as file: # Dışarıdan kaynak dosyasını okur.
        source_lines = file.readlines()
    # Yorum satırlarını ve boş satırları atar
    return [line.strip() for line in source_lines if line.strip() and not line.startswith('.')]


file_name = 'input.txt'

# Kaynak kod satırlarını dosyadan okur
source_lines = read_source_file(file_name)

intermediate_file = "intermediate.txt"


# Pass1'i kaynak kod satırları üzerinde çalıştırır
SYMTAB, start_address, program_length = pass1(source_lines)

# Sembol tablosunu belirtilen formatta çıktılar
for label, address in SYMTAB.items():
    print(f"{label} {address:04X}")

