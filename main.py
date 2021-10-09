import cmath
import math

degree_sign = u"\N{DEGREE SIGN}"
change_east = '\u0394''E'
change_north = '\u0394''N'
summation = '\u03A3'
c = 0.000262830755


# input the angle distance and store them in a dictionary
def prep_dist_angle(n):
    d = {}
    for i in range(n):
        name = input("Enter traverse point name: ")
        angle = input('Enter angle separated by space: ')
        distance = float(input("Enter the distance in meters (3dp): "))

        # function to convert angle to decimal degrees
        def dms2dd(degrees, minutes, seconds):
            dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60);
            return dd

        a = tuple(float(x) for x in angle.split())
        angle_decimal = dms2dd(a[0], a[1], a[2]).__round__(3)
        correct_distance = (distance - (distance * c)).__round__(3)
        d[name] = angle_decimal, correct_distance

    val = list(d.values())
    print(val)
    return val


n = int(input("How many traverse points do you have: "))
v = prep_dist_angle(n)


def eastings_northings(val):
    list_of_northings = []
    list_of_eastings = []

    # for loop to get the change in eastings and northings from the distances and angles provided
    # polar to rectangular. Format for input is (length, ‹angle in radians›).
    # Returns a complex number
    # test = [each for each ]
    for each in val:
        ang = each[0]
        dist = each[1]
        # print(ang)
        y = math.radians(ang)
        # print(y)
        cn1 = cmath.rect(dist, y)
        x = cn1.real
        x_round = x.__round__(3)
        print(change_north, x_round)
        list_of_northings.append(x_round)

        east = dist * cmath.sin(y).real
        east_round = east.__round__(3)
        print(change_east, east_round)
        list_of_eastings.append(east_round)
    return [list_of_eastings, list_of_northings]


w = eastings_northings(v)


def total_eastings_northings(w):
    sum_northings = round(sum(w[1]), 3)
    sum_eastings = round(sum(w[0]), 3)
    print('Sum of Northings: ', sum_northings)
    print('Sum of Eastings: ', sum_eastings)
    return sum_eastings, sum_northings


q = total_eastings_northings(w)


# getting the distance from the sum of northings and eastings using polar
def distance(sum_eastings, sum_northings):
    cn = complex(sum_northings, sum_eastings)
    y1 = cmath.polar(cn)
    y2 = y1[0].__round__(3)
    print('@', y2)
    return y2


f = distance(sum_eastings=q[0], sum_northings=q[1])


# getting the angle
def angle(sum_eastings, sum_northings):
    angle_rad = math.atan2(sum_eastings, sum_northings)
    angle_deg = (math.degrees(angle_rad)).__round__(3)
    if angle_deg < 0:
        angle_deg = angle_deg + 360

    print(angle_deg, degree_sign)
    return angle_deg


ray_trace_angle = angle(q[0], q[1])


# getting the difference of the northings and eastings of the control points
def control_points():
    cp1_northing = float(input("Enter northing of First control point: "))
    cp1_easting = float(input("Enter easting of First control point: "))

    cp2_northing = float(input("Enter northing of second control point: "))
    cp2_easting = float(input("Enter easting of second control point: "))

    cp_change_northing = (cp2_northing - cp1_northing).__round__(3)
    cp_change_easting = (cp2_easting - cp1_easting).__round__(3)
    print(cp_change_northing, cp_change_easting)
    return (cp_change_northing, cp_change_easting, cp1_northing, cp1_easting, cp2_northing, cp2_easting)


cp_eastings_northings = (control_points())
control_point_distance = distance(cp_eastings_northings[1], cp_eastings_northings[0])

control_point_angle = angle(cp_eastings_northings[1], cp_eastings_northings[0])

# #getting the bearing swing
b_swing = control_point_angle - ray_trace_angle
scale_factor = control_point_distance / f
#
print("Bearing Swing =", b_swing)
print("Scale Factor =", scale_factor)


#
# # add the bearing swing to each angle and multiply each corrected distance by the scale factor
def corrected_measurements():
    list_of_corrected_measurements = []
    for k in v:
        new_ang = k[0] + b_swing
        if new_ang > 360:
            new_ang = new_ang - 360
        new_dist = k[1] * scale_factor
        list_of_corrected_measurements.append((new_ang.__round__(3), new_dist.__round__(3)))
    print(list_of_corrected_measurements)
    return list_of_corrected_measurements


s = eastings_northings(corrected_measurements())
ray_trace_northing = cp_eastings_northings[2]
for q in s[1]:
    ray_trace_northing += q
    print("First control point plus change in northing: ", ray_trace_northing.__round__(3))

ray_trace_easting = cp_eastings_northings[3]
for e in s[0]:
    ray_trace_easting += e
    print("First control point plus change in easting: ", ray_trace_easting.__round__(3))

sum_corrected_northings = round(sum(s[1]), 3)
sum_corrected_eastings = round(sum(s[0]), 3)
print("Sum of corrected northings: ", sum_corrected_northings)
print("Sum of corrected eastings: ", sum_corrected_eastings)

corrected_northings = cp_eastings_northings[2] + sum_corrected_northings
corrected_eastings = cp_eastings_northings[3] + sum_corrected_eastings
print("Ray trace northings: ", corrected_northings.__round__(3))
print("Ray trace eastings: ", corrected_eastings.__round__(3))
print("Margin of error northings: ", ((corrected_northings.real).__round__(3) - cp_eastings_northings[4]).__round__(3))
print("Margin of error eastings: ", ((corrected_eastings).__round__(3) - cp_eastings_northings[5]).__round__(3))
print("Should be : ", cp_eastings_northings[4], cp_eastings_northings[5])
