const form = document.getElementById('word-form')
const input = document.getElementById('word-input')
const resultCard = document.getElementById('result-card')
const wordDisplay = document.getElementById('word-display')
const decodeDisplay = document.getElementById('decode-display')
const syllableCount = document.getElementById('syllable-count')
const stressIndex = document.getElementById('stress-index')
const badge = document.getElementById('cefr-badge')

const renderResult = (data) => {
  resultCard.classList.remove('hidden')
  wordDisplay.textContent = data.word
  decodeDisplay.textContent = data.decoding || data.word
  syllableCount.textContent = Array.isArray(data.syllables) ? data.syllables.length : 0
  stressIndex.textContent = String(data.stressed_syllable_index ?? 0)
  badge.textContent = data.cefr || 'A1'
  const color = {
    A1: '#0f9d58',
    A2: '#0f9d58',
    B1: '#ef8f20',
    B2: '#ef8f20',
    C1: '#d93025',
    C2: '#d93025'
  }[data.cefr || 'A1'] || '#0f9d58'
  badge.style.background = `${color}22`
  badge.style.color = color
}

const fetchAnalysis = async (word) => {
  const response = await fetch(`/api/analyze/${encodeURIComponent(word)}`)
  const data = await response.json()
  if (!response.ok) {
    throw new Error(data.error || 'Unable to analyze word.')
  }
  return data
}

form.addEventListener('submit', async (event) => {
  event.preventDefault()
  const word = input.value.trim()
  if (!word) {
    return
  }

  try {
    const data = await fetchAnalysis(word)
    renderResult(data)
  } catch (error) {
    resultCard.classList.remove('hidden')
    wordDisplay.textContent = 'Unavailable'
    decodeDisplay.textContent = error.message
    syllableCount.textContent = '0'
    stressIndex.textContent = '0'
    badge.textContent = 'ERR'
    badge.style.background = '#fbe8e8'
    badge.style.color = '#c62828'
  }
})

if (input.value.trim()) {
  form.requestSubmit()
}
