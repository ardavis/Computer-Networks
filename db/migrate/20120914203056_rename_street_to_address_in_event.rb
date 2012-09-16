class RenameStreetToAddressInEvent < ActiveRecord::Migration
  def change
    rename_column :events, :street, :address
  end
end
