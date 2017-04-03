require "stringer/version"

module Stringer
  def self.spacify *strings
      string = ""
      strings.each do |s|
          string += s + " "
      end
      string
  end

  def minify
  end

  def replacify
  end

  def tokenize
  end

  def removify
  end
end
