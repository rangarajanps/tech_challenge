output "3tier-ec2-ip" {
  value = "${aws_eip.instance.public_ip}"
}
