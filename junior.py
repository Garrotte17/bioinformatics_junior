def read_dna(file_path: str) -> str:
    try:
        with open(file_path, 'r') as dna:
            return dna.read()
    except FileNotFoundError:
        return file_path


def sequence_normalization(dna_sequence: str) -> str:
    return ''.join(nucleotide.upper() for nucleotide in dna_sequence if nucleotide not in {' ', '\n'})


def check_nucleotide(nucleotide: str) -> int:
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    return 0 if nucleotide in valid_nucleotides else 1


def find_longest_sequence(dna_sequence: str) -> dict:
    longest = {'sequence': '', 'count': 0}
    current = {'sequence': '', 'count': 0}

    for nucleotide in dna_sequence:
        if check_nucleotide(nucleotide):
            raise ValueError(f'ERROR: Incorrect nucleotide: {nucleotide}')

        if nucleotide == current['sequence']:
            current['count'] += 1
        elif current['count'] > longest['count']:
            longest = current.copy()
            current['sequence'] = nucleotide
            current['count'] = 1
        else:
            current['sequence'] = nucleotide
            current['count'] = 1

    return current if current['count'] > longest['count'] else longest


if __name__ == '__main__':
    DNA = read_dna(input("Последовательность ДНК или путь к файлу: "))
    result = find_longest_sequence(sequence_normalization(DNA))

    print(f'Найденная цепочка: "{result["sequence"] * result["count"]}"\nДлина цепочки {result["count"]}')
