def find_longest_sequence(dna_sequence):
    longest_sequence = ''
    current_sequence = ''

    for nucleotide in dna_sequence:
        if nucleotide in current_sequence:
            current_sequence += nucleotide
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = nucleotide

    return current_sequence if len(current_sequence) > len(longest_sequence) else longest_sequence


if __name__ == '__main__':
    dna = input("Последовательность ДНК: ")
    sequence_found = find_longest_sequence(dna)
    print(f'Найденная цепочка: "{sequence_found}"\nДлина цепочки {len(sequence_found)}')

