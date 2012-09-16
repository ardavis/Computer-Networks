class AddAddressToEvents < ActiveRecord::Migration
  def change
    remove_column :events, :location
    add_column :events, :street, :string
    add_column :events, :city, :string
    add_column :events, :state, :string
  end
end
