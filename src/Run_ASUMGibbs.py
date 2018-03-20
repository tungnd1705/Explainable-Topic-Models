import sys
import codecs
import ASUMGibbs


def read_voca_file(file_path):
    """
    Read vocabulary file
    :param file_path: The path of vocabulary file
    :return: vocabulary list
    """
    vocas = list()

    with codecs.open(file_path, "r", "utf-8") as voca_file:
        for each_line in voca_file:
            vocas.append(each_line.strip())

    return vocas


def main():
    try:
        document_file_path = sys.argv[1]
        voca_file_path = sys.argv[2]
        senti_words_prefix_path = sys.argv[3]
        output_file_name = sys.argv[4]
        topics = int(sys.argv[5])
    except IndexError:
        print("Usage: python {} document_file_path voca_file_path senti_words_prefix_path output_file_name topics".
              format(__file__))
        return

    vocas = read_voca_file(voca_file_path)

    senti_words = list()
    for senti_words_file_idx in range(3):
        senti_words_file_path = senti_words_prefix_path + str(senti_words_file_idx) + ".txt"
        senti_words.append(read_voca_file(senti_words_file_path))

    ASUM_Model = ASUMGibbs.ASUMGibbs(topics, senti_words, document_file_path, vocas)
    ASUM_Model.run(max_iter=2000)
    ASUM_Model.export_result(output_file_name)


if __name__ == '__main__':
    main()