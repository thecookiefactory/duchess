# -*- mode: ruby -*-

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :private_network, ip: "192.168.0.101"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision :shell, :path => "install-duchess.sh"
end
