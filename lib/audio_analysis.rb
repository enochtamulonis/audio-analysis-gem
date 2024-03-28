class AudioAnalysis
  def self.find_bpm(file_path)
    `pip install -r #{gem_path}/lib/python_analysis/requirements.txt`
    bpm = `python3 #{gem_path}/lib/python_analysis/bpm_analysis.py #{file_path}`
    bpm.to_f
  end

  def self.find_key(file_path)
    `pip install -r #{gem_path}/lib/python_analysis/requirements.txt`
    `python3 #{gem_path}/lib/python_analysis/key_analysis.py #{file_path}`
  end

  def self.analyze(file_path)
    `pip install -r #{gem_path}/lib/python_analysis/requirements.txt`
    bpm = `python3 #{gem_path}/lib/python_analysis/bpm_analysis.py #{file_path}`
    key =`python3 #{gem_path}/lib/python_analysis/key_analysis.py #{file_path}`
    { bpm: bpm, key: key }
  end

  private

  def self.gem_path
    Gem.loaded_specs["audio_analysis"].gem_dir
  end
end