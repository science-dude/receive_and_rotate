const listOfWords = [
  'ewordgam',
  'wordgame',
  'wordgame',
  'lyps',
  'psly',
  'slyp',
  'ypsl',
  'lips',
  'cyan',
  'tokyo',
  'god',
  'dog',
  'kyoto',
  'ogd',
];

const arguments = process.argv.slice(2);
if (!arguments.includes('logs')) {
  console.log = function () {};
}

const createSlyp = () => {
  const listOfUniqueWords = new Set();
  const wordLengthMap = new Map();

  const isAValidWord = (word) => {
    return word.length > 0 && /[a-zA-Z]/g.test(word);
  };
  const wasEvaluatedBefore = (word) => {
    return listOfUniqueWords.has(word);
  };
  const createRotationMap = (word) => {
    return new Map([[word, new Set([word])]]);
  };
  const searchForRotationSet = (wordLengthRotationMap, word) => {
    let wordRotationSet;
    for (let uniqueWord of wordLengthRotationMap.keys()) {
      if ((uniqueWord + uniqueWord).includes(word)) {
        // Is one of the rotations
        wordRotationSet = wordLengthRotationMap.get(uniqueWord);
      }
    }
    return wordRotationSet;
  };
  /**
   * Evaluates a word and stores it in the local scope if applicable.
   * @param {string} word
   */
  const receiveWord = (word) => {
    word = word.toLocaleLowerCase().trim();
    if (isAValidWord(word) && !wasEvaluatedBefore(word)) {
      console.log(`Added ${word} to the list of unique words`);
      listOfUniqueWords.add(word);

      if (!wordLengthMap.has(word.length)) {
        wordLengthMap.set(word.length, createRotationMap(word));
        return;
      }

      const wordLengthRotationMap = wordLengthMap.get(word.length);
      const wordRotationSet = searchForRotationSet(wordLengthRotationMap, word);

      if (wordRotationSet) {
        wordRotationSet.add(word);
      } else {
        wordLengthRotationMap.set(word, new Set([word]));
      }
    }
  };

  /**
   * Returns the list of set of rotations matching words.
   */
  const getRotations = () => {
    const allRotations = [];
    for (let lengthMap of wordLengthMap.values()) {
      for (let rotationSet of lengthMap.values()) {
        allRotations.push(Array.from(rotationSet.values()));
      }
    }
    return allRotations;
  };
  return {
    receiveWord: receiveWord,
    getRotations: getRotations,
  };
};

const slyp = createSlyp();
listOfWords.forEach((word) => slyp.receiveWord(word));
console.warn(slyp.getRotations());
