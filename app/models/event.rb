class Event < ActiveRecord::Base
  attr_accessible :desc, :name, :address, :city, :state, :date, :start_time, :end_time, :attendees_attributes

  has_many :attendees

  accepts_nested_attributes_for :attendees

  validates :name, presence: true
  validates :name, uniqueness: true

  def attendance
    if attendees.count.blank?
      0
    else
      attendees.count
    end
  end
end
