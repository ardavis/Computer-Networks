class Attendee < ActiveRecord::Base
  attr_accessible :name

  belongs_to :event

  validates :name, presence: true
end
