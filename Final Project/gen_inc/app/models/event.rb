class Event < ActiveRecord::Base
  attr_accessible :desc, :name, :street, :city, :state, :date, :start_time, :end_time

  validates :name, presence: true
  validates :name, uniqueness: true
end
