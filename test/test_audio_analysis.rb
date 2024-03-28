require "minitest/autorun"
require "audio_analysis"

class AudioAnalysisTest < Minitest::Test
  def test_find_bpm
    assert_equal("B", AudioAnalysis.find_key("test/audio.wav"))
  end
end